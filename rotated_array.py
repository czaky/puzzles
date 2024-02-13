# Puzzles related to rotated arrays/lists

import bs

def find_minimum(a: list) -> int:
    # A sorted array was rotated. Find the minimum element in O(log N)
    return a[bs.search(lambda m: a[m-1] < a[m] <= a[-1], 1, len(a)-1, 0)]
