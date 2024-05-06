"""Search Utils."""

from __future__ import annotations

from itertools import accumulate
from math import inf
from typing import Any, Callable


def upper_index(predicate: Callable, l: int, h: int, result: Any = None) -> Any:
    """Return the max index of an element for which `predicate` is True.

    Search starts between `l` and `h` markers.
    If `predicate` is True, `l` goes up, otherwise `h` goes down.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes index of the element.
    l : int
        lowest index to start search from (inclusive).
    h : int
        highest index to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.

    Returns
    -------
    Any
        The max index of an element which fulfills the predicate.

    """
    while l <= h:
        m = (l + h) // 2
        if predicate(m):
            result = m
            l = m + 1
        else:
            h = m - 1
    return result


def lower_index(predicate: Callable, l: int, h: int, result: Any = None) -> Any:
    """Return the min index of an element for which `predicate` is True.

    Search starts between `l` and `h` markers.
    If `predicate` is True, `h` goes down, otherwise `l` goes up.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes index of the element.
    l : int
        lowest index to start search from (inclusive).
    h : int
        highest index to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.

    Returns
    -------
    Any
        The max index of an element which fulfills the predicate.

    """
    while l <= h:
        m = (l + h) // 2
        if predicate(m):
            result = m
            h = m - 1
        else:
            l = m + 1
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
    l, h = start + 1, stop - 1
    # (abs difference, min-sum)
    mn = (csum[stop] - csum[start], csum[start])
    while l <= h:
        m = (l + h) // 2
        ls = csum[m] - csum[start]
        rs = csum[stop] - csum[m]
        if ls < rs:
            mn = min(mn, (rs - ls, ls))
            l = m + 1
        else:
            mn = min(mn, (ls - rs, rs))
            h = m - 1
    return mn[1], sum(mn)


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
    # Min difference between max and min of all 4 subsets.
    mn = inf
    # Iterate through all the possible splits,
    # and derive the minimum difference of sums of
    # the four subsets.
    # Since `[0, j)` needs at least 2 elements,
    # `j` needs to start at 2.
    # Since `[j, n)` needs at least 2 elements,
    # `j` needs to stop at `n-2`.
    for j in range(2, n - 1):
        # partition [0, j)
        w, x = partition_by_sum(csum, 0, j)
        # partition [j, n)
        y, z = partition_by_sum(csum, j, n)
        # w, y are the minimum subset sums
        # x, z are the maximum subset sums
        mn = min(mn, max(x, z) - min(w, y))

    return int(mn)
