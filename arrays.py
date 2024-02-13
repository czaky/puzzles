# Puzzles related to arrays/lists

import bs
from collections import Counter

def rotated_minimum(a: list) -> int:
    "A sorted list `a` was rotated. Find the minimum element in O(log N)."
    return a[bs.search(lambda m: a[m-1] < a[m] <= a[-1], 1, len(a)-1, 0)]

def equilibrium_point(a: list) -> int:
    "Index in `a` where sums of elements before and after are equal."
    # Uses binary search in O(log N).
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

def duplicates(a: list) -> list:
    "Return elements of the list `a` occurring more than once."
    return sorted((Counter(a) - Counter(set(a))).keys())