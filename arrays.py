"""Module for the array/list related puzzles."""

import math
from collections import Counter, deque
from typing import List, Optional, Tuple, Iterable
from functools import reduce, lru_cache
from operator import mul, neg, add
from itertools import accumulate, starmap, islice, chain
import search


def skip(it, n: int = 1):
    "Skip `n` elements in iterator `it`."
    return islice(it, n, None)


def minmax(t):
    "Return the min and max values of `t`."
    return min(t), max(t)


def subrev(a: list, s: int = 0, e: int = -1):
    "Reverse a subsequence of `a` from `s` to `e` (inclusive)."
    if s < 0:
        s += len(a)
    if e < 0:
        e += len(a)
    for i in range((1 + e - s) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]


def find_rotation(a: List[int]) -> int:
    "A sorted list `a` was rotated. Find the rotation index in O(log N)."
    return (search.binary(lambda m: a[m] <= a[-1], 0, len(a) - 1, -1) or 0) + 1


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
    return a[search.binary(lambda m: a[m - 1] > a[m], 1, len(a) - 1, len(a) - 1) or 0]


def duplicates(a: list) -> list:
    "Return elements of the list `a` occurring more than once."
    return sorted((Counter(a) - Counter(set(a))).keys())


def pairs_count(l: list, k: int) -> int:
    "Return the number of pairs of elements from `l` with sum of `k`."
    c = Counter(l)
    return sum(c[a] * (c[k - a] - int(a + a == k)) for a in c) // 2


def rotate(a: list, left: int = 1):
    "Rotate `a` inplace to the left."
    n = len(a)
    left %= n
    if left == 0:
        return
    subrev(a, 0, left - 1)
    subrev(a, left, n - 1)
    a.reverse()


def transition_point(a: list) -> int:
    "Transition index in sorted list `a` of '0's and '1's."
    return search.binary(lambda m: a[m] == 1, 0, len(a) - 1, -1) or 0


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
            mn = min(mn, abs(xi - yi))
    return mn if mn < len(a) else -1


def first_repeating_index(a: list):
    "Return index of the first repeating element in `a` else -1."
    c = Counter(a)
    return next((i for i, e in enumerate(a) if c[e] > 1), -1)


def dedup_sorted(a: list) -> int:
    "Remove duplicates in-place from a sorted list. Return end index."
    i = 1
    for j in range(1, len(a)):
        if a[j - 1] != a[j]:
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
        -1
        + (s[0] + d) // (d + 1)
        # We can seat ppl every (d + 1) seats
        + sum(-1 + (s[i] - s[i - 1]) // (d + 1) for i in range(1, len(s)))
        # [s[-1], n + (d+1)] we can seat ppl every (d + 1) seats.
        + (n - s[-1]) // (d + 1)
    )


def floor_element(a: List[int], x: int) -> int:
    "Return the largest element smaller or equal to `x` from sorted `a`."
    return search.binary(lambda m: a[m] > x, 0, len(a) - 1, -1) or 0


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
    p[zi] = reduce(mul, (e for i, e in enumerate(nums) if i != zi))
    return p


def count_triplets(a: List[int]) -> int:
    "Count distinct triplets on numbers in an array of distinct numbers."
    s = set(a)
    return sum(x < y and x + y in s for x in a for y in a)


def find_difference(a: List[int], d: int) -> bool:
    "True if there is an `e` from `a` where `d` - `e` is also in `a`."
    c = Counter(a)
    if 0 in c:
        return d in c
    return any(filter(lambda e: c[e + d] > int(d == 0), a))  # pyright: ignore


def pairs_equal_sum(a: List[int], b: List[int], s: int) -> list:
    "Return (sorted) pairs of elements from `a` and `b` with sum = `s`."
    sa = set(a)
    return sorted((s - y, y) for y in b if s - y in sa)


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
    return search.binary(lambda m: a[m] < b[m], 0, len(b) - 1, -1) + 1


def pascal_triangle_row(n: int) -> List[int]:
    "Return the nth row of pascal triangle."
    pr = [1] * n
    cr = [1] * n
    for i in range(2, n):
        cr, pr = pr, cr
        for j in range(1, i):
            cr[j] = pr[j - 1] + pr[j]
    return cr


def min_diff(a: List[int], k: int) -> int:
    "Smallest difference in a sublist of `a` of `k` elements."
    a.sort()
    return reduce(
        min, (a[i + k - 1] - a[i] for i in range(len(a) + 1 - k)), a[-1] - a[0]
    )


def selection_sort(a: List[int]):
    "Sort array `a` using selection sort."
    n = len(a)
    for i in range(n - 1):
        j = min(range(i, n), key=lambda j: a[j])
        a[i], a[j] = a[j], a[i]


def bubble_sort(a: List[int]):
    "Sort array `a` using bubble sort."
    n = len(a)
    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break


def duplicated_sorted_find_unique(a: List[int]) -> int:
    "In a sorted array find the unique one with every other duplicated."
    # 1 1 2 2 3 4 4 5 5
    # 1=1 2=2 3<4 4<5 5
    return a[
        search.binary(lambda m: a[2 * m] < a[2 * m + 1], 0, len(a) // 2 - 1, -1) * 2 + 2
    ]


def max_equal_zero_and_one_length(a: List[int]) -> int:
    "Return the max length of a sublist containing equal number of 0 and 1."
    d = {0: -1}
    return reduce(
        max,
        (
            j - d.setdefault(cs, j)
            for j, cs in enumerate(accumulate(map(lambda x: 2 * x - 1, a)))
        ),
        0,
    )


def toys_with_budget(a: List[int], b: int) -> int:
    "Returns number of toys from `a` that can be bought with budget `b`."
    return next((i for i, c in enumerate(accumulate(sorted(a))) if c > b), len(a))


def first_last(a: List[int], x: int) -> Tuple[int, int]:
    "Return the first and last index of `x` in a sorted array `a`."
    l: int = search.binary(lambda m: a[m] >= x, 0, len(a) - 1, -1) + 1
    h: int = search.binary(lambda m: a[m] > x, l, len(a) - 1, -1) + 0
    return (l, h) if l <= h else (-1, -1)


def merge_sorted(a: List[int], b: List[int]):
    "Merge two sorted lists in place. `a` gets the lower elements."
    l = min(len(a), len(b))
    a[: -l - 1 : -1], b[:l] = zip(*map(minmax, zip(reversed(a), b)))
    a.sort()
    b.sort()


def meta_frog_jumps(frogs: List[int], pads: int) -> int:
    "Return min hops for `frogs` traversing `pads`, jumping over each other."
    frogs.sort()
    jumps = pads - frogs[-1]
    for fi in range(1, len(frogs)):
        jumps += frogs[fi] - frogs[fi - 1]
    return jumps


def min_partition_diff(a: List[int]) -> int:
    "Minimum difference between two partitions of `a`."
    s = sum(a)

    @lru_cache(None)
    def rec(i, s1):
        if i < 0:
            return abs(s - 2 * s1)
        return min(rec(i - 1, s1 + a[i]), rec(i - 1, s1))

    return rec(len(a) - 1, 0)


def max_histogram_rectangle(h: list) -> int:
    "Return the max rectangular area under the histogram `h`."
    s = []

    def it(j, v=0):
        while s and h[s[-1]] > v:
            yield h[s.pop()] * ((j - s[-1] - 1) if s else j)
        s.append(j)
        yield 0

    return max(chain(map(max, starmap(it, enumerate(h))), it(len(h))))


def max_matrix_area(m: List[List[int]]) -> int:
    "Matrix `m` contains 1 and 0. Find the largest rectangle."

    def hist(h, r):
        h[:] = ((x + 1) * y for x, y in zip(h, r))
        return h

    return max(map(max_histogram_rectangle, accumulate(m, hist, initial=m[0][:])))


def median2(a: List[int], b: List[int]) -> float:
    "Return median of two lists `a` and `b` in O(log N)."
    if len(a) > len(b):
        a, b = b, a
    n = len(a) + len(b)
    if n == 0:
        return 0
    l, h = 0, len(a)
    p = (n + 1) // 2
    if h == 0:
        return b[p - 1] if n % 2 else (b[p - 1] + b[p]) / 2

    while l <= h:
        ma = (l + h) // 2
        mb = p - ma

        la = a[ma - 1] if ma > 0 else -math.inf
        lb = b[mb - 1] if mb > 0 else -math.inf
        ra = a[ma] if ma < len(a) else math.inf
        rb = b[mb] if mb < len(b) else math.inf

        if la <= rb and lb <= ra:
            y, x = max(la, lb), min(ra, rb)
            return y if n % 2 else (x + y) / 2

        if la > rb:
            h = ma - 1
        else:
            l = ma + 1

    return 0


def max_sub_sum(a: Iterable[int]) -> int:
    "Return the max sum of a sub-array from `a`."
    # Kadane’s Algorithm
    return max(accumulate(a, lambda x, y: max(0, x + y), initial=0))


def max_circular_sub_sum(a: List[int]) -> int:
    "Return the max sum of a circular sub-array from `a`."
    return max(max_sub_sum(a), max_sub_sum(map(neg, a)) + sum(a)) or max(a)


def kaiten_sushi(belt: List[int], distance: int) -> int:
    "Count dishes on the `belt` which are unique within the `distance`."
    dishes = set()
    order = deque()
    count = 0
    for d in belt:
        if d in dishes:
            continue
        count += 1
        dishes.add(d)
        order.append(d)
        if len(dishes) > distance:
            dishes.remove(order.popleft())
    return count


def mail_room_theft(arrivals: List[int], cost: int, theft: float) -> float:
    """
    Retrieve arriving packages from mail room at `cost` of entering
    and in face of `theft` factor.

    Each time the packages are retrieved from the mail room a `cost` needs
    to be paid. There is a probability of `theft` with each new arrival,
    where the packages stored before disappear.

    Return the expected collected value of retrieved packages.
    """
    mr = [0]  # mail_room_value
    cl = [0]  # collected value
    for p in arrivals:
        # theft plus new package
        mr[:] = (int(mrv * (1 - theft) + p) for mrv in mr)
        # pickup
        cl.append(max(map(add, mr, cl)) - cost)
        mr.append(0)
    return max(cl)


def next_smallest_palindrome_number(num: list) -> list:
    """
    Return the next smallest palindrome number from `num`.

    Num is a sequence of digits [0-9].
    """
    n = len(num)
    if n == 0:
        return []
    if all(d == 9 for d in num):
        # 9..9 => 10..01
        return [1] + ([0] * (n - 1)) + [1]

    i, j = (n - 1) // 2, n // 2
    while i >= 0 and num[i] == num[j]:
        i -= 1
        j += 1
    if i < 0:
        # original is a palindrome
        # look for the next one
        i, j = 0, n - 1
        num[-1] += 1
    if num[i] < num[j]:
        # Cannot copy directly.
        i, j = (n - 1) // 2, n // 2
        num[i] += 1
    # Copy remaining digits.
    while i >= 0:
        if num[i] >= 10:
            num[i] -= 10
            num[i - 1] += 1
        num[j] = num[i]
        i -= 1
        j += 1
    return num


def aggressive_cows(stalls: list, cows: int) -> int:
    "Return maximum possible distance between `cows` when placed into the `stalls`."
    stalls.sort()
    ac = lambda d: lambda a, s: s - a[1] >= d and (a[0] + 1, s) or a
    gt = lambda d: cows > reduce(ac(d), stalls, (1, stalls[0]))[0]
    return search.binary(gt, 1, stalls[-1] - stalls[0]) + 0


def smaller_on_right_count(arr: list) -> list:
    "Return a list counting elements smaller that each element in `arr`."
    n = len(arr)
    o = [0] * n
    x = list(range(n))
    t = x[:]

    def merge(l, m, h):
        k, i, j = l, l, m + 1
        while i <= m and j <= h:
            if arr[t[i]] > arr[t[j]]:
                o[t[i]] += h - j + 1
                x[k] = t[i]
                i += 1
            else:
                x[k] = t[j]
                j += 1
            k += 1
        x[k : h + 1] = i <= m and t[i : m + 1] or t[j : h + 1]
        t[l : h + 1] = x[l : h + 1]

    def split(i, j):
        if i < j:
            m = (i + j) // 2
            split(i, m)
            split(m + 1, j)
            merge(i, m, j)

    split(0, len(arr) - 1)

    return o


def min_sum_split(a: list, k: int) -> int:
    "Split `a` in `k` sub-lists. Minimize the maximum sum of every one."
    # Search through possible splits of `a` given the maximum `mx` sum of each sub-list.
    # Calculate the number of splits given the `mx` maximum sum of elements.
    acc = lambda mx: lambda a, e: (e, a[1] + 1) if a[0] + e > mx else (a[0] + e, a[1])
    # Assure that the number of splits is less or equal to k
    fit = lambda mx: k < reduce(acc(mx), a, (0, 1))[1]
    # Use binary search to find the maximum sub-sum.
    return search.binary_lt(fit, max(a), sum(a)) + 0


def out_ouf_there_number(a: List[int]) -> int:
    "Smallest positive number not in the array `a` or not a sum of elements from `a`."
    a.sort()
    # Looking for the lowest number between `a[i]...a[i+1]` that cannot be represented
    # by numbers `a[0] ... a[i]` in any way as a sum.
    # For `a[i]` such number must be larger than `a[i]` and any other number added before.
    # Even if there were gaps in the array up to `a[i]`, those have been filled already
    # by another sum of previous numbers.
    # Thus we compare the array itself and the cumulative value starting at 1.
    return next((s for e, s in zip(a, accumulate(a, initial=1)) if s < e), sum(a) + 1)


def max_min_window(a: List[int]) -> List[int]:
    "For every window size return the maximum of the minimums."
    # The idea is to find a window size for each element, where the
    # element is the minimum. Larger elements have smaller window size.
    # This is done by finding the index for the left and right element
    # that is smaller than the current element.
    #
    # Using: [10, 20, 30, 50, 10, 70, 30] as example.

    def bracket(b: List[int], it: Iterable[int]) -> List[int]:
        "Computes the left and right index of a smaller element."
        s = []  # Contains indexes of elements smaller and the previous one.
        for i in it:
            # Remove all elements larger or equal to this one.
            while s and a[i] <= a[s[-1]]:
                s.pop()
            if s:
                # s[-1] should contain the index of an element smaller
                # than the current one.
                b[i] = s[-1]
            s.append(i)
        return b

    n = len(a)
    # The left index of a smaller element is initialized with -1.
    left = bracket([-1] * n, range(n))
    # => [-1, 0, 1, 2, -1, 4, 4]

    # The right index is initialized with `n` (= 7).
    right = bracket([n] * n, reversed(range(n)))
    # => [7, 4, 4, 4, 7, 6, 7]

    wnd = [0] * n
    for e, l, r in zip(a, left, right):
        # Assign the element to the window size where it is the minimum.
        # It two elements share the same window size, take the maximum of both.
        # `(r - l - 2)` - size of the window with exclusive indexes `r` and `l`
        # minus one for the 0-based indexing.
        wnd[r - l - 2] = max(wnd[r - l - 2], e)
    # => [70, 30, 20, 0, 0, 0, 10]

    for i in reversed(range(n - 1)):
        # If an element is the maximum in a larger window,
        # it needs to be considered a maximum for smaller windows as well.
        wnd[i] = max(wnd[i], wnd[i + 1])
    # => [70, 30, 20, 10, 10, 10, 10]

    return wnd


def partition_equal_sum(a: List[int], k: int) -> bool:
    "Partition `a` into `k` subset with equal sum value."
    # The idea is to compute the sum of numbers recursively
    # for each state denoted by '2**len(a)' bits.
    # Each bit indicates that a number is in the state or not.

    @lru_cache(None)
    def value(state: int) -> int:
        for i, e in enumerate(a):
            # Check if the number `e` is in this state.
            if state & (1 << i):
                # Then compute the value for a state without it.
                v = value(state ^ (1 << i))
                # Check if we can fit the new number under the target.
                if v + e <= target:
                    # Return the sum for this bin (modulo target)
                    return (v + e) % target
        # Return target to indicate failure or return 0 for an empty `state`.
        return target if state else 0

    target, r = divmod(sum(a), k)
    # If there is a reminder, then the array does not fit into `k` bins.
    # Otherwise, a valid `value` will be less than the `target` returned above.
    return not r and value((1 << len(a)) - 1) < target


def candy(r: List[int]) -> int:
    """Given ratings `r` reward each kid with candies.
    If a child is better than its neighbor it get more candies.
    Each child gets at least 1 candy.

    Return number of candies needed.
    """
    n = len(r)
    c = accumulate(range(n), lambda a, i: i and r[i] > r[i - 1] and a + 1 or 0)
    d = accumulate(range(n), lambda a, i: i and r[-i - 1] > r[-i] and a + 1 or 0)
    return sum(max(x, y) for x, y in zip(c, reversed(list(d)))) + n
