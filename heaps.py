"""Module contains puzzles related to heaps."""

from __future__ import annotations

from heapq import heapify, heappop, heappush, heappushpop


def connect_ropes_cost(a: list[int]) -> int:
    """Connect ropes of lengths in `a` into single one reducing the cost.

    Cost of connecting two ropes is equal to the sum of their lengths.
    """
    heapify(a)
    c = 0
    while len(a) > 1:
        nr = heappop(a) + heappop(a)
        heappush(a, nr)
        c += nr
    return c


def smallest_intersecting_range(arrays: list[list[int]]) -> tuple[int, int]:
    """Return the smallest range that intersects the sorted `arrays`."""
    # The idea is to keep track of numbers from the `arrays` on the heap,
    # always increasing the lowest number with the next on the same array.
    # This approach tries to minimize the span of numbers on the heap.
    # The heap then always has the `min` and `max` values so far, which
    # allow us to determine the running smallest range.

    # Start with the lowest number in each array.
    h: list[tuple[int, list, int]] = [(a[0], a, 1) for a in arrays]
    heapify(h)  # make a min-heap out of the values

    # The minimum is always h[0], but we need to track the heap max.
    h_max = max(h)[0]  # max value on the heap, so far
    h_min, a, c = heappop(h)  # heap-minimum, array, next column
    # The range is stored as `(<length>, <start>)`,
    # which allows to easily run `min` on it.
    min_range = (h_max - h_min, h_min)  # minimum range, so far

    # Once we cannot add any more numbers from an array,
    # we abort, since otherwise the range would not include
    # numbers from that particular array and would be incorrect.
    while c < len(a):
        # `c` points to the next column.
        h_max = max(h_max, a[c])
        h_min, a, c = heappushpop(h, (a[c], a, c + 1))
        min_range = min(min_range, (h_max - h_min, h_min))

    return min_range[1], sum(min_range)
