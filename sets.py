"""Code related to sets and puzzels on sets."""

from __future__ import annotations

from itertools import chain, combinations
from operator import itemgetter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator, Sequence


class Disjoint:
    """Create a disjoint set using find-union algorithms."""

    def __init__(self, size: int) -> None:
        """Initialize the disjoint set to the `size` of nodes specified.

        Parameters
        ----------
        size : int
            the number of nodes in the set

        """
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size

    def find(self, i: int) -> int:
        """Find the representative node for `i`."""
        while i != self.parent[i]:
            i, self.parent[i] = self.parent[i], self.parent[self.parent[i]]
        return i

    def union(self, i: int, j: int) -> int:
        """Merge both subsets containing nodes `i` and `j`."""
        x = self.find(i)
        y = self.find(j)

        if x == y:
            return x

        rx = self.rank[x]
        ry = self.rank[y]

        # rename x to the larger set.
        if rx < ry or (rx == ry and self.size[x] < self.size[y]):
            x, y = y, x
        # x has a rank larger or equal to y.
        # attach y under x
        self.parent[y] = x
        # since x is now root of both trees
        # adjust the rank, if the trees were of equal height
        if rx == ry:
            self.rank[x] += 1
        self.size[x] += self.size[y]

        return x


def weighted_paths_in_tree(edges: list[Sequence[int]], queries: list[int]) -> list[int]:
    """Given a list of weighted edges and a list of queries, return counts of paths.

    Each query specifies the maximum weight of edges that can count in paths.
    Connections between edges count un-directed as only once.
    """
    # Determine number of nodes.
    n = max(max(x, y) for x, y, _ in edges)
    # Initialize the disjoint-set.
    parents = list(range(n + 1))
    sizes = [1] * (n + 1)

    def parent(n: int) -> int:
        """Find the parent of n. Compress the path."""
        while n != parents[n]:
            # Compress the set by halving.
            n, parents[n] = parents[n], parents[parents[n]]
        return n

    def union(x: int, y: int) -> int:
        """Connect `x` and `y` into one set. Return number of new paths."""
        x, y = parent(x), parent(y)
        if x == y:
            return 0
        # New paths possible by connecting `sizes[x]` with `sizes[y]` nodes.
        paths = sizes[x] * sizes[y]
        # Use the larger set as parent. Should improve the find `parent` function.
        if sizes[x] < sizes[y]:
            x, y = y, x
        # The parent now contains `sizes[y]` nodes.
        sizes[x] += sizes[y]
        # Attach `y` to `x`
        parents[y] = x
        return paths

    # Sort the edges by weight.
    edges.sort(key=itemgetter(2))
    results = [0] * len(queries)
    paths = 0  # number of paths so far.
    start = 0  # starting edge index to be processed.
    # Sort the queries by weight.
    for i, q in sorted(enumerate(queries), key=itemgetter(1)):
        # Add all edges weighting less or equal than the current query.
        while start < len(edges) and edges[start][2] <= q:
            x, y, _ = edges[start]
            # Accumulate the count of new paths for each edge added.
            paths += union(x, y)
            start += 1
        results[i] = paths
    return results


def powerset(iterable: Iterable) -> Iterator:
    """powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)."""  # noqa: D402
    s = set(iterable)
    for size in range(len(s)):
        yield from map(set, combinations(s, size))
    yield s


def merge_email_accounts(accounts: list[list[str]]) -> list[list[str]]:
    """Merge email accounts using email addresses.

    The `accounts` is a list of accounts of this format:
    ```
       ["<name>", "<email_0>", "<email_1>", "<email_2>"]
    ```

    Accounts are merged if they share at least one email.
    Merged accounts contain the union of email addresses.

    Parameters
    ----------
    accounts : list[str]
        A list of accounts containing name and email addresses.

    Returns
    -------
    list[str]
        A list of merged accounts with sorted email list.

    """
    n = len(accounts)
    parents = list(range(n))

    def parent(n: int) -> int:
        """Find the parent of n. Compress the path."""
        while n != parents[n]:
            # Compress the set by halving.
            n, parents[n] = parents[n], parents[parents[n]]
        return n

    emails = {}
    for i, a in enumerate(accounts):
        for e in a[1:]:
            parents[i] = i = parent(emails.setdefault(e, i))  # noqa: PLW2901

    merged = [[] for _ in range(n)]
    for e, i in emails.items():
        merged[parent(i)].append(e)
    any(map(list.sort, merged))
    return sorted([accounts[i][0], *m] for i, m in enumerate(merged) if m)

def crazy_chemist_mix(mixes: list, explosive: list) -> list:
    """Mix compounds from the `mixes` list. Avoid mixing `explosive` combinations.

    Mixed ingredients build a joint set. Adding an ingredient to another,
    adds it to the mix that the ingredient is already in. Ultimately,
    this is a disjoint set problem resulting in sets that don't combine
    any ingredients from the `explosive` list.

    Parameters
    ----------
    mixes : list
        pairs of ingredients to mix
    explosive : list
        pairs of ingredients to avoid

    Returns
    -------
    list
        a list of 0s and 1s, indicating when it is safe to mix ingredients
        for each entry in the `mixes` list.

    """
    n = max(max(a, b) for a, b in chain(mixes, explosive)) + 1
    parents = list(range(n))
    size = [1] * n

    def parent(x: int) -> int:
        """Find the parent of `x`. Compress the path."""
        while x != parents[x]:
            # Compress the set by halving.
            x, parents[x] = parents[x], parents[parents[x]]
        return x

    emap = [set() for _ in range(n)]
    for x, y in explosive:
        emap[x].add(y)
        emap[y].add(x)
    safety = []
    for a, b in mixes:
        a, b = parent(a), parent(b)  # noqa: PLW2901
        if a == b:
            safety.append(1)
            continue
        if a in emap[b] or b in emap[a]:
            # mixing a and b would produce an explosive mix
            safety.append(0)
            continue
        safety.append(1)
        if size[a] < size[b]:
            a, b = b, a  # noqa: PLW2901
        parents[b] = a
        size[a] += size[b]
        if emap[a] or emap[b]:
            emap[a] = emap[b] = set(map(parent, chain(emap[a], emap[b])))
    return safety
