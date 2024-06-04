"""Search Utils."""

from __future__ import annotations

import sys
from itertools import accumulate
from typing import Any, Callable


def upper_index(predicate: Callable, low: int, high: int, result: Any = None) -> Any:
    """Return the max index of an element for which `predicate` is True.

    Search starts between `low` and `high` markers.
    If `predicate` is True, `low` goes up, otherwise `high` goes down.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes index of the element.
    low : int
        lowest index to start search from (inclusive).
    high : int
        highest index to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.

    Returns
    -------
    Any
        The max index of an element which fulfills the predicate.

    """
    while low <= high:
        m = low + (high - low) // 2
        if predicate(m):
            result = m
            low = m + 1
        else:
            high = m - 1
    return result


def lower_index(predicate: Callable, low: int, high: int, result: Any = None) -> Any:
    """Return the min index of an element for which `predicate` is True.

    Search starts between `low` and `high` markers.
    If `predicate` is True, `high` goes down, otherwise `low` goes up.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes index of the element.
    low : int
        lowest index to start search from (inclusive).
    high : int
        highest index to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.

    Returns
    -------
    Any
        The max index of an element which fulfills the predicate.

    """
    while low <= high:
        m = low + (high - low) // 2
        if predicate(m):
            result = m
            high = m - 1
        else:
            low = m + 1
    return result


def upper_bound(
    predicate: Callable,
    low: float,
    high: float,
    result: Any = None,
    e: float | None = None,
) -> Any:
    """Return the max value between `[low, high]` for which `predicate` is True.

    Search starts between `low` and `high` markers.
    If `predicate` is True, `low` goes up, otherwise `high` goes down.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes value between `[low, high]`.
    low : float
        lowest value to start search from (inclusive).
    high : float
        highest value to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.
    e: float | None
        epsilon value used in the search.

    Returns
    -------
    Any
        The max value which fulfills the predicate.

    """
    e = e or sys.float_info.epsilon
    while high - low > e:
        m = (low + high) / 2
        if predicate(m):
            low = result = m
        else:
            high = m - e
    return result


def lower_bound(
    predicate: Callable,
    low: float,
    high: float,
    result: Any = None,
    e: float | None = None,
) -> Any:
    """Return the min value between `[low, high]` for which `predicate` is True.

    Search starts between `low` and `high` markers.
    If `predicate` is True, `high` goes dow, otherwise `low` goes up.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes value between `[low, high]`.
    low : float
        lowest value to start search from (inclusive).
    high : float
        highest value to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.
    e: float | None
        epsilon value used in the search.

    Returns
    -------
    Any
        The min value which fulfills the predicate.

    """
    e = e or sys.float_info.epsilon
    while high - low > e:
        m = (low + high) / 2
        if predicate(m):
            high = result = m
        else:
            low = m + e
    return result


def largest_sum_cycle(edges: list[int]) -> int:
    """Return the max node index sum of cycles in graph defined by `edges`."""
    # Simplest recursive solution in `O(|E|)`.
    # For each cycle we compute the total path sum reached so far.
    # This allows us to remove any tangling prefix nodes from the sum.
    # At the same time the `edges` are marked as dead-end.
    # This allows the code to run in `O(|E|)`

    # Contains the sums of the paths.
    v = [-1] * len(edges)

    def visit(i: int, s: int) -> int:
        if edges[i] < 0:
            return -1
        s += i
        if v[i] >= 0:
            # Remove any prefix from the sum.
            return s - v[i]
        # Mark the cell with the sum so far.
        v[i] = s
        result = visit(edges[i], s)
        # Mark the cell as dead-end to prevent revisits.
        edges[i] = -1
        return result

    return max(visit(i, 0) for i in range(len(edges)))


def geek_cake_distribution(chunks: list[int], k: int) -> int:
    """Divide a cake into k slices. Return the sweetness of the least sweet slice."""

    def slices(min_sweetness: int) -> int:
        sc = 0  # slices-count
        ss = 0  # slice-sweetness
        for s in chunks:
            ss += s
            if ss >= min_sweetness:
                sc += 1
                ss = 0
        return sc

    return upper_index(lambda m: k <= slices(m), min(chunks), sum(chunks), 0)


def find_rotation(a: list[int]) -> int:
    """Find the rotation index in O(log N) of a sorted, then rotated list `a`."""
    return upper_index(lambda m: a[m] > a[-1], 0, len(a) - 1, -1) + 1


def rotated_minimum(a: list) -> int:
    """Find the min element in O(log N) of a sorted, then rotated list `a`."""
    return a[find_rotation(a)]


def bitonic_point(a: list[int]) -> int:
    """Maximum of strictly increasing array then maybe strictly decreasing."""
    # Runs in O(log N)
    return a[upper_index(lambda m: a[m - 1] <= a[m], 1, len(a) - 1, len(a) - 1)]


def transition_point(a: list) -> int:
    """Transition index in sorted list `a` of '0's and '1's."""
    return upper_index(lambda m: a[m] != 1, 0, len(a) - 1, -1)


def floor_element(a: list[int], x: int) -> int:
    """Return the largest element smaller or equal to `x` from sorted `a`."""
    return upper_index(lambda m: a[m] <= x, 0, len(a) - 1, -1)


def find_extra_element(a: list[int], b: list[int]) -> int:
    """Return index of an extra element in sorted arrays `a` and `b`."""
    # Runs in O(log N)
    return upper_index(lambda m: a[m] == b[m], 0, min(len(a), len(b)) - 1, -1) + 1


def duplicated_sorted_find_unique(a: list[int]) -> int:
    """In a sorted array find the unique one with every other duplicated."""
    # 1 1 2 2 3 4 4 5 5
    # 1=1 2=2 3<4 4<5 5
    return a[
        upper_index(lambda m: a[2 * m] == a[2 * m + 1], 0, len(a) // 2 - 1, -1) * 2 + 2
    ]


def first_last(a: list[int], x: int) -> tuple[int, int]:
    """Return the first and last index of `x` in a sorted array `a`."""
    l: int = lower_index(lambda m: a[m] >= x, 0, len(a) - 1, len(a))
    h: int = upper_index(lambda m: a[m] <= x, l, len(a) - 1, -1)
    return (l, h) if l <= h else (-1, -1)


def equilibrium_point(a: list) -> int:
    """Index in `a` where sums of elements before and after are equal."""
    # O(N)
    # See partition_by sum for O(log N) approach.
    l = 0
    h = len(a) - 1
    l_sum = 0
    h_sum = 0
    while l < h:
        if l_sum < h_sum:
            l_sum += a[l]
            l += 1
        else:
            h_sum += a[h]
            h -= 1
    if l_sum == h_sum:
        return l
    return -1


def partition_by_sum(
    csum: list[int],
    start: int = 0,
    stop: int | None = None,
) -> tuple[int, int]:
    """Partition the array a so the sums left and right are closest.

    Parameters
    ----------
    csum : List[int]
        List of cumulative integers to partition, starting with 0.
    start : int, optional
        Start index on the array to consider, by default 0
    stop : int | None, optional
        Exclusive stop index on the array to consider, by default None

    Returns
    -------
    Tuple[int, int]
        The left and right sum, sorted.

    """
    # O(log N) approach, if the `csum` array is available in advance.
    # See `equilibrum_point` for a O(N) approach.
    if stop is None:
        stop = len(csum) - 1
    # This assumes that `csum` is derived from array `a` by this process:
    #    `csum = list(accumulate(a, initial=0))`
    # `csum` is longer than `a` by 1, with leading 0.
    #  starting at second element, stopping at second to last.
    msum2 = csum[start] + csum[stop]
    # Closest point to `msum2 / 2`?
    m = lower_index(lambda m: csum[m] << 1 >= msum2, start + 1, stop - 1, stop)
    # Use the midpoint...
    if csum[m - 1] + csum[m] < msum2:
        return csum[stop] - csum[m], csum[m] - csum[start]
    # or the point before it.
    return csum[m - 1] - csum[start], csum[stop] - csum[m - 1]


def four_partitions_min_sum_difference(a: list[int]) -> int:
    """Partition `a` into four sub-lists.

    Return sub-lists' minimum sum difference.
    Sub-lists need to be non-empty and continuous.

    Parameters
    ----------
    a : List[int]
        A list of integers to partition.

    Returns
    -------
    int
        Minimum difference of sums in the partition.

    """
    n = len(a)
    # Using csum to lover the search time to: O(N * log N)
    csum = [0, *accumulate(a)]
    parts = lambda j: (*partition_by_sum(csum, 0, j), *partition_by_sum(csum, j, n))
    return min(max(xyzw) - min(xyzw) for xyzw in map(parts, range(2, n - 1)))

def water_distribution(a: list[int], b: list[int], d: list[int]) -> list[tuple]:
    """Return a summary of pipes going through houses and their min diameter.

    Lists `a` to `b` describe the connectivity,
    while list `d` describes the pipe diameter between $a_i$ to $b_i$.

    Parameters
    ----------
    a : list
        List with indexes of the starting house for each pipe.
    b : list
        List with indexes of the ending house for each pipe.
    d : list
        List with the diameter of the pipe between $a_i$ and $b_i$.

    Returns
    -------
    list
        A list of triples for each connected sequence of pipes with the info:
          * starting house index
          * ending house index
          * minimum diameter of pipes between the start and end.

    """
    # This is a rather simple as there is only one pipe starting, going through,
    # or ending at a specific house, thus there is no branching involved.
    # The idea is to determine the starting index, with no upstream connection,
    # and following the adjacency map to the end. At the same time the diameter
    # for each sequence is minimized.

    # Build adjacency maps and record diameter of outgoing pipes.
    n = max(*a, *b)
    adj = [0] * (n + 1)
    dia = adj[:]
    for x, y, z in zip(a, b, d):
        adj[x] = y
        dia[y] = z

    pipes = []
    # Find the starting point ...
    for x, y in enumerate(adj):
        if y == 0 or dia[x] != 0:
            continue
        s, e = x, y
        md = dia[e]
        while adj[e]:
            e = adj[e]
            md = min(md, dia[e])
        pipes.append((s, e, md))
    return pipes
