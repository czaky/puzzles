"""Search Utils."""

from __future__ import annotations

import sys
from heapq import heappop, heappush
from itertools import accumulate
from typing import Any, Callable


def upper_int(predicate: Callable, low: int, high: int, result: Any = None) -> Any:
    """Find the max int from between `low` and `high` for which `predicate` is True.

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


def lower_int(predicate: Callable, low: int, high: int, result: Any = None) -> Any:
    """Find the min int from between `low` and `high` for which `predicate` is True.

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

    return upper_int(lambda m: k <= slices(m), min(chunks), sum(chunks), 0)


def find_rotation(a: list[int]) -> int:
    """Find the rotation index in O(log N) of a sorted, then rotated list `a`."""
    return upper_int(lambda m: a[m] > a[-1], 0, len(a) - 1, -1) + 1


def rotated_minimum(a: list) -> int:
    """Find the min element in O(log N) of a sorted, then rotated list `a`."""
    return a[find_rotation(a)]


def bitonic_point(a: list[int]) -> int:
    """Maximum of strictly increasing array then maybe strictly decreasing."""
    # Runs in O(log N)
    return a[upper_int(lambda m: a[m - 1] <= a[m], 1, len(a) - 1, len(a) - 1)]


def transition_point(a: list) -> int:
    """Transition index in sorted list `a` of '0's and '1's."""
    return upper_int(lambda m: a[m] != 1, 0, len(a) - 1, -1)


def floor_element(a: list[int], x: int) -> int:
    """Return the largest element smaller or equal to `x` from sorted `a`."""
    return upper_int(lambda m: a[m] <= x, 0, len(a) - 1, -1)


def find_extra_element(a: list[int], b: list[int]) -> int:
    """Return index of an extra element in sorted arrays `a` and `b`."""
    # Runs in O(log N)
    return upper_int(lambda m: a[m] == b[m], 0, min(len(a), len(b)) - 1, -1) + 1


def duplicated_sorted_find_unique(a: list[int]) -> int:
    """In a sorted array find the unique one with every other duplicated."""
    # 1 1 2 2 3 4 4 5 5
    # 1=1 2=2 3<4 4<5 5
    return a[
        upper_int(lambda m: a[2 * m] == a[2 * m + 1], 0, len(a) // 2 - 1, -1) * 2 + 2
    ]


def first_last(a: list[int], x: int) -> tuple[int, int]:
    """Return the first and last index of `x` in a sorted array `a`."""
    low: int = lower_int(lambda m: a[m] >= x, 0, len(a) - 1, len(a))
    high: int = upper_int(lambda m: a[m] <= x, low, len(a) - 1, -1)
    return (low, high) if low <= high else (-1, -1)


def equilibrium_point(a: list) -> int:
    """Index in `a` where sums of elements before and after are equal."""
    # O(N)
    # See partition_by sum for O(log N) approach.
    low = 0
    high = len(a) - 1
    l_sum = 0
    h_sum = 0
    while low < high:
        if l_sum < h_sum:
            l_sum += a[low]
            low += 1
        else:
            h_sum += a[high]
            high -= 1
    if l_sum == h_sum:
        return low
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
    m = lower_int(lambda m: csum[m] << 1 >= msum2, start + 1, stop - 1, stop)
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


def shortest_path_with_special_edge(edges: list, a: int, b: int) -> int:
    """Return the shortest path distance from `a` to `b` using `edges`.

    `edges` contains a list of edge specifications: `(n1, n2, w1, w2)`, where
    `n1` and `n2` are the numeric nodes and `w1` and `w2` are weights of the
    normal edge and a special ("curved") edge.

    The search can only return path distances using at most one of the
    special edges. The edges are considered unidirectional.

    Parameters
    ----------
    edges : list
        list of elements of the type `(n1, n2, w1, w2)`.
    a : int
        start node index
    b : int
        final node index

    Returns
    -------
    int
        minimum path distance using at most one special edge.

    """
    # Determine the size of the adjacency map.
    n = max(max(e[0], e[1]) for e in edges) + 1
    # Build up the adjacency map.
    adj = [[] for _ in range(n)]
    for e in edges:
        adj[e[0]].append(e[1:])
        adj[e[1]].append((e[0], e[2], e[3]))
    # Initialize the minimum visited distance.
    mx = sum(e[2] for e in edges) + 1
    v = [[mx, mx] for _ in range(n)]
    # Priority heap queue: distance, number of special edges, node
    q = [(0, 0, a)]
    while q:
        # Distance, number of special edges, destination node.
        d, s, n = heappop(q)
        # Cut if shorter value found.
        if v[n][s] <= d:
            continue
        # This will be the min distance to b.
        if n == b:
            return d
        # Update minimum visited distance.
        v[n][s] = v[n][1] = d
        for c, e1, e2 in adj[n]:
            # Cut, if there exists a better path.
            if v[c][s] > d + e1:
                heappush(q, (d + e1, s, c))
                # In case we did not use the curved edge yet,
                # and it is shorter than the straight one.
                if s == 0 and e2 < e1 and v[c][1] > d + e2:
                    heappush(q, (d + e2, 1, c))
    return -1

def flower_gardening(a: list[int], k: int, w: int) -> int:
    """Return the maximum length of the shortest flower in a after `k` days of watering.

    The flowers of height `a` are watered every of the `k` days, but each day
    only successive `w` flowers can be watered.

    Parameters
    ----------
    a : list[int]
        Array of initial flower heights.
    k : int
        Number of days the flowers are watered.
    w : int
        The width of the window used each day to water the flowers.

    Returns
    -------
    int
        The maximum hight of the shortest flower after `k` days.

    """
    # The idea is to find the upper bound of the flower height
    # for flowers that can grow up to h.
    # This is done by introducing a predicate function `can grow`
    # and applying binary search.
    # Overall: O(n * ln k) time complexity.
    n = len(a)

    def can_grow(h: int) -> bool:
        """Determine if plants can grow up to `h` in `k` days."""
        # The function uses a sliding window where each flower is
        # watered for as many days as needed to reach `h`.
        # The additional height is propagated to the next flower.
        # In order to only water `w` flowers for `diff` days,
        # the same `diff` number is subtracted from the `i + w` flower.
        # O(n) time complexity.
        aux = [0] * (n + 1)
        days = 0
        for i, e in enumerate(a):
            h += aux[i]
            diff = h - e - days
            if diff <= 0:
                continue
            days += diff
            if days > k:
                return False
            aux[min(i + w, n)] = diff
        return True

    return upper_int(can_grow, min(a), min(a) + k)
