# Puzzles related to rotated arrays/lists

import bs

def find_minimum(l: list) -> int:
    # A sorted array was rotated. Find the minimum element in O(log N)
    return l[bs.search(lambda m: arr[m-1] < arr[m] <= arr[-1], 1, n-1, 0)]