"Module contains puzzles related to heaps."

from heapq import heapify, heappush, heappop
from typing import List, Tuple


def connect_ropes_cost(a: List[int]) -> int:
    """
    Connect ropes of lengths in `a` into single one reducing the cost.
    Cost of connecting two ropes is equal to the sum of their lengths.
    """
    heapify(a)
    c = 0
    while len(a) > 1:
        nr = heappop(a) + heappop(a)
        heappush(a, nr)
        c += nr
    return c


def smallest_intersecting_range(arrays: List[List[int]]) -> Tuple[int, int]:
    "Return the smallest range that intersects the sorted `arrays`."
    # The idea is to keep track of numbers from the `arrays` on the heap,
    # always increasing the lowest number with the next on the same array.
    # This approach tries to minimize the span of numbers on the heap.
    # The heap then always has the `min and max values so far, which
    # allow us to determine the running smallest range.

    # Start with the lowest number in each array.
    h = [(a[0], a, int(1)) for a in arrays]
    heapify(h)  # min-heap

    # The minimum is always h[0], but we need to track the heap max.
    mxh = max(h)[0]  # max value on the heap, so far

    # The range is stored as `(<length>, <start>)`,
    # which allows to easily run `min` on it.
    mnr = (mxh - h[0][0], h[0][0])  # minimum range, so far

    while h:
        v, a, c = heappop(h)
        mnr = min(mnr, (mxh - v, v))
        # Once we cannot add any more numbers from a list,
        # we abort, otherwise the range would not include
        # numbers from that particular list and would be invalid.
        if c == len(a):
            break
        heappush(h, (a[c], a, c + 1))
        mxh = max(mxh, a[c])

    return mnr[1], mnr[0] + mnr[1]
