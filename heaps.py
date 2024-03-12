"Module contains puzzles related to heaps."

from heapq import heapify, heappush, heappop
from typing import List


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
