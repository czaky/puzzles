"""Module for the array/list related puzzles."""

from collections import Counter
from typing import List, Optional, Tuple
from functools import reduce
from operator import mul
from itertools import accumulate
from iter import skip
import search as bs

def subrev(a: list, s: int=0, e: int=-1):
    "Reverse a subsequence of `a` from `s` to `e` (inclusive)."
    if s<0:
        s += len(a)
    if e<0:
        e += len(a)
    for i in range((1 + e - s) // 2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

def find_rotation(a: List[int]) -> int:
    "A sorted list `a` was rotated. Find the rotation index in O(log N)."
    return bs.binary(lambda m: a[m] <= a[-1], 0, len(a)-1, -1) + 1

def rotated_minimum(a: list) -> int:
    "A sorted list `a` was rotated. Find the minimum element in O(log N)."
    return a[find_rotation(a)]

def equilibrium_point(a: list) -> int:
    "Index in `a` where sums of elements before and after are equal."
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

def bitonic_point(a: List[int]) -> int:
    "Maximum of strictly increasing array then maybe strictly decreasing."
    # Runs in O(log N)
    return a[bs.binary(lambda m: a[m-1] > a[m], 1, len(a)-1, len(a)-1)]

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
        # [1 - (d+1), S[0]] we can seat ppl every (d + 1) seats
        -1 + (s[0] + d) // (d + 1) +
        # We can seat ppl every (d + 1) seats
        sum(-1 + (s[i] - s[i-1]) // (d + 1) for i in range(1, len(s))) +
        # [s[-1], n + (d+1)] we can seat ppl every (d + 1) seats.
        (n - s[-1]) // (d + 1))

def floor_element(a: List[int], x: int) -> int:
    "Return the largest element smaller or equal to `x` from sorted `a`."
    return bs.binary(lambda m: a[m] > x, 0, len(a)-1, -1)

def product_except_self(nums: List[int]) -> List[int]:
    """
Return an array where each element is the product of nums
except for the element at the given index.
"""
    pr = reduce(mul, nums)
    if pr:
        return [pr // e for e in nums]
    zi = nums.index(0)
    p = [0] * len(nums)
    p[zi] = reduce(mul, (e for i,e in enumerate(nums) if i != zi))
    return p

def count_triplets(a: List[int]) -> int:
    "Count distinct triplets on numbers in an array of distinct numbers."
    s = set(a)
    return sum(x < y and x+y in s for x in a for y in a)

def find_difference(a: List[int], d: int) -> bool:
    "True if there is an `e` from `a` where `d` - `e` is also in `a`."
    c = Counter(a)
    if 0 in c:
        return d in c
    return next(filter(lambda e: c[e + d] > int(d == 0), a), False)

def pairs_equal_sum(a: List[int], b: List[int], s: int) -> list:
    "Return (sorted) pairs of elements from `a` and `b` with sum = `s`."
    sa = set(a)
    return sorted((s-y, y) for y in b if s-y in sa)

def greater_smaller(a: List[int]) -> Optional[int]:
    "Return element greater than all previous and smaller than all following."
    mn = skip(accumulate(reversed(a), min))
    it = skip(zip(reversed(list(mn)), accumulate(a, max)))
    return next((n for n, x in it if n == x), None)

def smallest_sub_with_greater_sum(a: List[int], k: int) -> int:
    "Returns smallest sublist length with sum above `k`."
    i = 0
    s = 0
    n = len(a)
    ln = n + 1
    for j, e in enumerate(a):
        s += e
        while s > k:
            ln = min(ln, j - i + 1)
            s -= a[i]
            i += 1
    return ln if ln < n + 1 else 0

def window_distinct_count(a: List[int], k: int) -> List[int]:
    "Returns count of distinct elements for every `k` window in `a`."
    if k > len(a):
        return []
    d = {}
    for i in range(k):
        d[a[i]] = d.get(a[i], 0) + 1

    n = len(a)
    cnt = [0] * (n - k + 1)
    cnt[0] = len(d)
    for i in range(n - k):
        # delete beginning
        c1 = a[i]
        d[c1] -= 1
        if d[c1] == 0:
            del d[c1]
        # add ending
        c2 = a[i + k]
        d[c2] = d.get(c2, 0) + 1
        # update count array
        cnt[i + 1] = len(d)
    return cnt

def find_extra_element(a: List[int], b: List[int]) -> int:
    "Return index of an extra element in sorted arrays `a` and `b`."
    # Runs in O(log N)
    if len(a) < len(b):
        a, b = b, a
    return bs.binary(lambda m: a[m] < b[m], 0, len(b) - 1, -1) + 1

def pascal_triangle_row(n: int) -> List[int]:
    "Return the nth row of pascal triangle."
    pr = [1] * n
    cr = [1] * n
    for i in range(2, n):
        cr, pr = pr, cr
        for j in range(1, i):
            cr[j] = pr[j-1] + pr[j]
    return cr

def min_diff(a: List[int], k: int) -> int:
    "Smallest difference in a sublist of `a` of `k` elements."
    a.sort()
    d = a[-1] - a[0]
    k -= 1
    for i in range(len(a) - k):
        d = min(d, a[i+k] - a[i])
    return d

def selection_sort(a: List[int]):
    "Sort array `a` using selection sort."
    n = len(a)
    for i in range(n-1):
        j = min(range(i, n), key=lambda j: a[j])
        a[i], a[j] = a[j], a[i]

def bubble_sort(a: List[int]):
    "Sort array `a` using bubble sort."
    n = len(a)
    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break

def duplicated_sorted_find_unique(a: List[int]) -> int:
    "In a sorted array find the unique one with every other duplicated."
    # 1 1 2 2 3 4 4 5 5
    # 1=1 2=2 3<4 4<5 5
    return a[bs.binary(lambda m: a[2*m]<a[2*m+1], 0, len(a)//2 -1, -1)*2 + 2]

def max_equal_zero_and_one_length(a: List[int]) -> int:
    "Return the max length of a sublist containing equal number of 0 and 1."
    d = {0:-1}
    return reduce(max, (
        j - d.setdefault(cs, j)
        for j, cs in enumerate(accumulate(map(lambda x: 2*x-1, a)))), 0)

def toys_with_budget(a: List[int], b: int) -> int:
    "Returns number of toys from `a` that can be bought with budget `b`."
    return next(
        (i for i, c in enumerate(accumulate(sorted(a))) if c > b), len(a))

def first_last(a: List[int], x: int) -> Tuple[int, int]:
    "Return the first and last index of `x` in a sorted array `a`."
    l = bs.binary(lambda m: a[m] >= x, 0, len(a)-1, -1) + 1
    h = bs.binary(lambda m: a[m] > x, l, len(a)-1, -1)
    return (l, h) if l<=h else (-1,-1)

def minmax(t):
    "Return the min and max values of `t`."
    return min(t), max(t)

def merge(a: List[int], b: List[int]):
    "Merge two sorted lists in place. `a` gets the lower elements."
    l = min(len(a), len(b))
    a[:-l-1:-1], b[:l] = zip(*map(minmax, zip(reversed(a), b)))
    a.sort()
    b.sort()

def meta_frog_jumps(frogs: List[int], pads: int) -> int:
    "Return min hops for `frogs` traversing `pads`, jumping over each other."
    frogs.sort()
    jumps = pads - frogs[-1]
    for fi in range(1, len(frogs)):
        jumps += frogs[fi] - frogs[fi-1]
    return jumps
