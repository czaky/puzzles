"""Module for the array/list related puzzles."""

from collections import Counter
from typing import List
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

def min_distance(a: list, x: int, y: int) -> int:
    "Minimum index based distance between `x` and `y` in `a`."
    xi = yi = -1
    mn = len(a)
    for i, e in enumerate(a):
        measure = False
        if e == x:
            xi = i
            measure = yi >= 0
        if e == y:
            yi = i
            measure = xi >= 0
        if measure:
            mn = min(mn, abs(xi-yi))
    return mn if mn < len(a) else -1

def first_repeating_index(a: list):
    "Return index of the first repeating element in `a` else -1."
    c = Counter(a)
    return next((i for i, e in enumerate(a) if c[e] > 1), -1)

def dedup_sorted(a: list) -> int:
    "Remove duplicates in-place from a sorted list. Return end index."
    i = 1
    for j in range(1, len(a)):
        if a[j-1] != a[j]:
            a[i] = a[j]
            i += 1
    return i

def meta_cafeteria(n: int, d: int, s: List[int]) -> int:
    """
Return number of new diners to be seated at distance `d` from
each other at a row of `n` seats. `s` is a list of taken seats.
Seats are counted as [1 .. N] inclusive
"""
    s.sort()
    return (
        # [1 - (d+1), S[0]] we can seat diners every (d + 1) seats
        -1 + (s[0] + d) // (d + 1) +
        # We can seat a diner ever (d + 1) seats
        sum(-1 + (s[i] - s[i-1]) // (d + 1) for i in range(1, len(s))) +
        # [s[-1], n + (d+1)] we can seat diners ever (d + 1) seats.
        (n - s[-1]) // (d + 1))

def list_floor(a: List[int], x: int) -> int:
    "Return the largest element smaller or equal to `x` from sorted `a`."
    return bs.binary(lambda m: a[m] > x, 0, len(a)-1, -1)
