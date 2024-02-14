"""Module for the array/list related puzzles."""

from collections import Counter
import search as bs

def subrev(a: list, s: int=0, e: int=-1):
    "Reverse a subsequence of `a` from `s` to `e` (inclusive)."
    if s<0:
        s += len(a)
    if e<0:
        e += len(a)
    for i in range((1 + e - s) // 2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

def rotated_minimum(a: list) -> int:
    "A sorted list `a` was rotated. Find the minimum element in O(log N)."
    return a[bs.binary(lambda m: a[m-1] < a[m] <= a[-1], 1, len(a)-1, 0)]

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

def pairs_count(l: list, k: int) -> int:
    "Return the number of pairs of elements from `l` with sum of `k`."
    c = Counter(l)
    return sum(c[a] * (c[k-a] - int(a+a == k)) for a in c) // 2

def rotate(a: list, left: int=1):
    "Rotate `a` inplace to the left."
    n = len(a)
    left %= n
    if left == 0:
        return
    subrev(a, 0, left-1)
    subrev(a, left, n-1)
    a.reverse()

def transition_point(a: list) -> int:
    "Transition index in sorted list `a` of '0's and '1's."
    return bs.binary(lambda m: a[m] == 1, 0, len(a) - 1, -1)
