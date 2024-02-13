# Binary Search

from typing import Optional
from collections.abc import Callable

def gt(gt: Callable, l: int, h: int, i: int=None) -> Optional[int]:
"""Returns the index of an element which is NOT greater than (`gt`).

Arguments:
    gt  - greater than predicate; takes index of the element. 
    l   - lowest index to start search from (inclusive).
    h   - highest index to start search from (inclusive).
    i   - default index to return (`None` by default).
"""
    while l <= h:
        m = (l+h)//2
        if gt(m):
            h = m - 1
        else:
            i = m
            l = m + 1
    return i