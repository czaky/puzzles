"Code related to sets and puzzels on sets."

from typing import List, Sequence
from operator import itemgetter
from itertools import combinations


class Disjoint:
    "Create a disjoint set using find-union algorithms."

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size

    def find(self, i) -> int:
        "Find the representative node for `i`."
        while i != self.parent[i]:
            i, self.parent[i] = self.parent[i], self.parent[self.parent[i]]
        return i

    def union(self, i, j) -> int:
        "Merge both subsets containing nodes `i` and `j`."
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


def weighted_paths_in_tree(edges: List[Sequence[int]], queries: List[int]) -> List[int]:
    """Given a list of weighted edges and a list of queries, return count of paths for each query.

    Each query specifies the maximum weight of edges that can count in paths.
    Connections between edges count un-directed as only once.
    """
    # Determine number of nodes.
    n = max(max(x, y) for x, y, _ in edges)
    # Initialize the disjoint-set.
    parents = list(range(n + 1))
    sizes = [1] * (n + 1)

    def parent(n: int) -> int:
        "Find the parent of n. Compress the path."
        while n != parents[n]:
            # Compress the set by halving.
            n, parents[n] = parents[n], parents[parents[n]]
        return n

    def union(x: int, y: int) -> int:
        "Connect `x` and `y` into one set. Return number of new paths."
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


def powerset(iterable):
    "powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = set(iterable)
    for size in range(len(s)):
        yield from map(set, combinations(s, size))
    yield s
