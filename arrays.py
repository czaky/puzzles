"""Module for the array related puzzles."""

from __future__ import annotations

from collections import Counter, deque
from functools import lru_cache, reduce
from itertools import accumulate, chain, islice, starmap
from math import inf
from operator import add, mul, neg
from typing import Any, Callable, Iterable, Iterator

from search import lower_index, upper_index


def skip(it: Iterable, n: int = 1) -> Iterator:
    """Skip `n` elements in iterator `it`."""
    return islice(it, n, None)


def minmax(t: Iterable) -> tuple:
    """Return the min and max values of `t`."""
    return min(t), max(t)


def subrev(a: list, s: int = 0, e: int = -1) -> None:
    """Reverse a subsequence of `a` from `s` to `e` (inclusive)."""
    if s < 0:
        s += len(a)
    if e < 0:
        e += len(a)
    for i in range((1 + e - s) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]


def duplicates(a: list) -> list:
    """Return elements of the list `a` occurring more than once."""
    return sorted((Counter(a) - Counter(set(a))).keys())


def pairs_count(l: list, k: int) -> int:
    """Return the number of pairs of elements from `l` with sum of `k`."""
    c = Counter(l)
    return sum(c[a] * (c[k - a] - int(a + a == k)) for a in c) // 2


def rotate(a: list, left: int = 1) -> None:
    """Rotate `a` inplace to the left."""
    n = len(a)
    left %= n
    if left == 0:
        return
    subrev(a, 0, left - 1)
    subrev(a, left, n - 1)
    a.reverse()


def min_distance(a: list, x: int, y: int) -> int:
    """Minimum index based distance between `x` and `y` in `a`."""
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


def first_repeating_index(a: list) -> int:
    """Return index of the first repeating element in `a` else -1."""
    c = Counter(a)
    return next((i for i, e in enumerate(a) if c[e] > 1), -1)


def dedup_sorted(a: list) -> int:
    """Remove duplicates in-place from a sorted list. Return end index."""
    i = 1
    for j in range(1, len(a)):
        if a[j - 1] != a[j]:
            a[i] = a[j]
            i += 1
    return i


def meta_cafeteria(n: int, d: int, s: list[int]) -> int:
    """Return a number of new diners to be seated at the table.

    The diners need to be seated at distance `d` from
    each other at a row of `n` seats. `s` is a list of taken seats.
    Seats are counted as [1 .. N] inclusive.

    Parameters
    ----------
    n : int
        Length of the row of seats.
    d : int
        Min distance between diners.
    s : list[int]
        Seats taken

    Returns
    -------
    int
        Number of new diners that can be seated at distance d.

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


def product_except_self(nums: list[int]) -> list[int]:
    """Return a product array leaving elements from `nums` out at their index.

    Parameters
    ----------
    nums : list[int]
        List of inteagers.

    Returns
    -------
    list[int]
        Products of the numbers with nums left out of the product at
        their corresponding index.

    """
    pr = reduce(mul, nums)
    if pr:
        return [pr // e for e in nums]
    zi = nums.index(0)
    p = [0] * len(nums)
    p[zi] = reduce(mul, (e for i, e in enumerate(nums) if i != zi))
    return p


def count_triplets(a: list[int]) -> int:
    """Count distinct triplets on numbers in an array of distinct numbers."""
    s = set(a)
    return sum(x < y and x + y in s for x in a for y in a)


def find_difference(a: list[int], d: int) -> bool:
    """Return true if there is an `e` from `a` where `d` - `e` is also in `a`."""
    c = Counter(a)
    if 0 in c:
        return d in c
    return any(filter(lambda e: c[e + d] > int(d == 0), a))  # pyright: ignore


def pairs_equal_sum(a: list[int], b: list[int], s: int) -> list:
    """Return (sorted) pairs of elements from `a` and `b` with sum = `s`."""
    sa = set(a)
    return sorted((s - y, y) for y in b if s - y in sa)


def greater_smaller(a: list[int]) -> int | None:
    """Return element greater than all previous and smaller than all following."""
    mn = skip(accumulate(reversed(a), min))
    it = skip(zip(reversed(list(mn)), accumulate(a, max)))
    return next((n for n, x in it if n == x), None)


def smallest_sub_with_greater_sum(a: list[int], k: int) -> int:
    """Return smallest sublist length with sum above `k`."""
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


def window_distinct_count(a: list[int], k: int) -> list[int]:
    """Return count of distinct elements for every `k` window in `a`."""
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


def pascal_triangle_row(n: int) -> list[int]:
    """Return the nth row of pascal triangle."""
    pr = [1] * n
    cr = [1] * n
    for i in range(2, n):
        cr, pr = pr, cr
        for j in range(1, i):
            cr[j] = pr[j - 1] + pr[j]
    return cr


def min_diff(a: list[int], k: int) -> int:
    """Smallest difference in a sublist of `a` of `k` elements."""
    a.sort()
    return reduce(
        min, (a[i + k - 1] - a[i] for i in range(len(a) + 1 - k)), a[-1] - a[0]
    )


def selection_sort(a: list[int]) -> None:
    """Sort array `a` using selection sort."""
    n = len(a)
    for i in range(n - 1):
        j = min(range(i, n), key=lambda j: a[j])
        a[i], a[j] = a[j], a[i]


def bubble_sort(a: list[int]) -> None:
    """Sort array `a` using bubble sort."""
    n = len(a)
    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break


def max_equal_zero_and_one_length(a: list[int]) -> int:
    """Return the max length of a sublist containing equal number of 0 and 1."""
    d = {0: -1}
    return reduce(
        max,
        (
            j - d.setdefault(cs, j)
            for j, cs in enumerate(accumulate(2 * x - 1 for x in a))
        ),
        0,
    )


def toys_with_budget(a: list[int], b: int) -> int:
    """Return number of toys from `a` that can be bought with budget `b`."""
    return next((i for i, c in enumerate(accumulate(sorted(a))) if c > b), len(a))


def merge_sorted(a: list[int], b: list[int]) -> None:
    """Merge two sorted lists in place. `a` gets the lower elements."""
    l = min(len(a), len(b))
    a[: -l - 1 : -1], b[:l] = zip(*map(minmax, zip(reversed(a), b)))
    a.sort()
    b.sort()


def meta_frog_jumps(frogs: list[int], pads: int) -> int:
    """Return min hops for `frogs` traversing `pads`, jumping over each other."""
    frogs.sort()
    jumps = pads - frogs[-1]
    for fi in range(1, len(frogs)):
        jumps += frogs[fi] - frogs[fi - 1]
    return jumps


def min_partition_diff(a: list[int]) -> int:
    """Minimum difference between two partitions of `a`."""
    s = sum(a)

    @lru_cache(None)
    def rec(i: int, s1: int) -> int:
        if i < 0:
            return abs(s - 2 * s1)
        return min(rec(i - 1, s1 + a[i]), rec(i - 1, s1))

    return rec(len(a) - 1, 0)


def max_histogram_rectangle(h: list) -> int:
    """Return the max rectangular area under the histogram `h`."""
    s = []

    def it(j: int, v: int = 0) -> Iterator:
        while s and h[s[-1]] > v:
            yield h[s.pop()] * ((j - s[-1] - 1) if s else j)
        s.append(j)
        yield 0

    return max(chain(map(max, starmap(it, enumerate(h))), it(len(h))))


def max_matrix_area(m: list[list[int]]) -> int:
    """Matrix `m` contains 1 and 0. Find the largest rectangle."""

    def hist(h: list, r: list) -> list:
        h[:] = ((x + 1) * y for x, y in zip(h, r))
        return h

    return max(map(max_histogram_rectangle, accumulate(m, hist, initial=m[0][:])))


def median2(a: list[int], b: list[int]) -> float:
    """Return median of two lists `a` and `b` in O(log N)."""
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

        la = a[ma - 1] if ma > 0 else -inf
        lb = b[mb - 1] if mb > 0 else -inf
        ra = a[ma] if ma < len(a) else inf
        rb = b[mb] if mb < len(b) else inf

        if la <= rb and lb <= ra:
            y, x = max(la, lb), min(ra, rb)
            return y if n % 2 else (x + y) / 2

        if la > rb:
            h = ma - 1
        else:
            l = ma + 1

    return 0


def max_sub_sum(a: Iterable[int]) -> int:
    """Return the max sum of a sub-array from `a`."""
    # Kadane`s Algorithm
    return max(accumulate(a, lambda x, y: max(0, x + y), initial=0))


def max_circular_sub_sum(a: list[int]) -> int:
    """Return the max sum of a circular sub-array from `a`."""
    return max(max_sub_sum(a), max_sub_sum(map(neg, a)) + sum(a)) or max(a)


def max_sum_substring(s: str, d: dict) -> str:
    """Return the substring of `s` with max sum, with character values from `d`."""
    # Kadane`s Algorithm
    # Transform `s` into a numeric array
    num = lambda c: d.get(c, ord(c))
    # Calculate the cumulative Kadane's value.
    acc = accumulate(map(num, s), lambda x, y: max(0, x + y), initial=0)
    # Determine the max value interval.
    # i - last zero-index, mv - max value, mi mj - max value's indexes
    i = mv = mi = mj = 0
    # j - current index, v - current value.
    for j, v in enumerate(acc):
        if v == 0:
            i = j
        elif mv < v:
            mv, mi, mj = v, i, j
    # Return the substring or if empty, return the highest (negative) character.
    return s[mi:mj] if mi < mj else max(s, key=num)


def zero_sum_sub_max_len(a: list[int]) -> int:
    """Return the max length of a sub-array of `a` which sums to zero."""
    # The idea is to compute an array of the accumulated values.
    # If any accumulated value shows up in the array again, there is a zero sub-array.
    # Store the accumulated values to prevent recomputation below.
    acc = list(accumulate(a))
    # Determine the first occurrence of the sum.
    # Special care is given for an empty array with 0 having -1 as index.
    occ = {0: -1}
    for i, e in enumerate(acc):
        occ.setdefault(e, i)
    # Determine the longest span between this occurrence and the first one.
    return max(starmap(lambda i, e: i - occ[e], enumerate(acc)))


def zero_sum_sub_max_interval(a: list[int]) -> tuple[int, int]:
    """Return the indexes of the longest sub-array of `a` which sums to zero."""
    # The idea is to compute an array of the accumulated values.
    # If any accumulated value shows up in the array again, there is a zero sub-array.
    # Store the accumulated values to prevent recomputation below.
    acc = list(accumulate(a))
    # Determine the first occurrence of the sum.
    # Special care is given for an empty array with 0 having -1 as index.
    occ = {0: -1}
    for i, e in enumerate(acc):
        occ.setdefault(e, i)
    # Determine the longest span between this occurrence and the first one.
    # Sort by length and the lowest column first. Length is negative here.
    length, j = min(starmap(lambda j, e: (occ[e] - j, j), enumerate(acc)))
    return j + 1 + length, j + 1


def kaiten_sushi(belt: list[int], distance: int) -> int:
    """Count dishes on the `belt` which are unique within the `distance`."""
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


def mail_room_theft(arrivals: list[int], cost: int, theft: float) -> float:
    """Retrieve arriving packages from mail room at specific `cost`.

    You need to take into account the `cost` of entering
    and face the `theft` factor.

    Each time the packages are retrieved from the mail room a `cost` needs
    to be paid. There is a probability of `theft` with each new arrival,
    where the packages stored before disappear.

    Return the expected collected value of retrieved packages.

    Parameters
    ----------
    arrivals : list[int]
        A list of scheduled package arrivals.
    cost : int
        Cost deduced each time the mail-root is entered.
    theft : float
        A probability that the packages are stollen from the mail-room each day.

    Returns
    -------
    float
        Collected value minus the accumulated cost.

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
    """Return the next smallest palindrome number from `num`.

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
    """Return maximum possible distance between `cows` when placed into the `stalls`."""
    stalls.sort()
    ac = lambda d: lambda a, s: s - a[1] >= d and (a[0] + 1, s) or a
    le = lambda d: cows <= reduce(ac(d), stalls, (1, stalls[0]))[0]
    return upper_index(le, 1, stalls[-1] - stalls[0])


def min_sum_split(a: list, k: int) -> int:
    """Split `a` in `k` sub-lists. Minimize the maximum sum of every one."""
    # Search through possible splits of `a` given the maximum `mx` sum of each sub-list.
    # Calculate the number of splits given the `mx` maximum sum of elements.
    acc = lambda mx: lambda a, e: (e, a[1] + 1) if a[0] + e > mx else (a[0] + e, a[1])
    # Assure that the number of splits is less or equal to k
    fit = lambda mx: k >= reduce(acc(mx), a, (0, 1))[1]
    # Use binary search to find the maximum sub-sum.
    return lower_index(fit, max(a), sum(a))


def smaller_on_right_counts(arr: list) -> list:
    """Return a list counting elements smaller that each element in `arr`."""
    # This uses merge-sort count-inversion to count the unsorted elements.
    n = len(arr)
    # Output array
    o = [0] * n
    # Index arrays using for sorting `arr`.
    # This avoids actually overriding `arr`.
    x = list(range(n))
    t = x[:]

    def merge(l: int, m: int, h: int) -> None:
        # k - number of sorted entries.
        # i - index into the first half.
        # j - index into the second half (m + 1).
        k, i, j = l, l, m + 1
        # Iterate through both halves.
        while i <= m and j <= h:
            # The elements in both halves are sorted in reverse order.
            # IF element on the left is larger than on the right,
            if arr[t[i]] > arr[t[j]]:
                # then remaining elements in the right half are smaller
                # than `arr[t[i]]` as well and the number of unsorted elements
                # is the number of remaining elements on the right.
                o[t[i]] += h - j + 1
                # Keep track of sorted indexes.
                x[k] = t[i]
                i += 1
            else:
                # Keep track of sorted indexes.
                x[k] = t[j]
                j += 1
            k += 1
        # Fill the rest of the `x` array.
        # If i <= m, all remaining elements on the left are smaller
        # and all the elements on the right were sorted into `x`.
        # Otherwise, left was sorted into `x` and all the remaining
        # elements from the right are smaller than the rest.
        x[k : h + 1] = t[i : m + 1] if i <= m else t[j : h + 1]
        # Copy over this part into the temporary array.
        t[l : h + 1] = x[l : h + 1]

    def split(i: int, j: int) -> None:
        if i < j:
            m = (i + j) // 2
            split(i, m)
            split(m + 1, j)
            merge(i, m, j)

    split(0, len(arr) - 1)
    return o


def unsorted_pairs_count(a: list) -> int:
    """Return a count of unsorted element pairs in `a`."""
    # This uses merge-sort count inversion to count the unsorted elements.
    # See `smaller_on_the_right` count above for the same function returning an array.

    t = a[:]

    def merge(l: int, m: int, h: int) -> int:
        o = 0
        # k - number of sorted entries.
        # i - index into the first half.
        # j - index into the second half (m + 1).
        k, i, j = l, l, m + 1
        # Iterate through both halves.
        while i <= m and j <= h:
            # The elements in both halves are sorted in reverse order.
            # IF element on the left is larger than on the right,
            if t[i] > t[j]:
                # then remaining elements in the right half are smaller
                # than `arr[t[i]]` as well and the number of unsorted elements
                # is the number of remaining elements on the right.
                o += h - j + 1
                # Keep track of sorted indexes.
                a[k] = t[i]
                i += 1
            else:
                # Keep track of sorted indexes.
                a[k] = t[j]
                j += 1
            k += 1
        # Fill the rest of the `x` array.
        # If i <= m, all remaining elements on the left are smaller
        # and all the elements on the right were sorted into `x`.
        # Otherwise, left was sorted into `x` and all the remaining
        # elements from the right are smaller than the rest.
        a[k : h + 1] = t[i : m + 1] if i <= m else t[j : h + 1]
        # Copy over this part into the temporary array.
        t[l : h + 1] = a[l : h + 1]
        return o

    def split(i: int, j: int) -> int:
        if i < j:
            m = (i + j) // 2
            return split(i, m) + split(m + 1, j) + merge(i, m, j)
        return 0

    return split(0, len(a) - 1)


def out_ouf_there_number(a: list[int]) -> int:
    """Smallest positive number not a sum of elements from `a`."""
    a.sort()
    # Looking for the lowest number between `a[i]...a[i+1]` that cannot be represented
    # by numbers `a[0] ... a[i]` in any way as a sum.
    # For `a[i]` such number must be larger than `a[i]` and others number added before.
    # Even if there were gaps in the array up to `a[i]`, those have been filled already
    # by another sum of previous numbers.
    # Thus we compare the array itself and the cumulative value starting at 1.
    return next((s for e, s in zip(a, accumulate(a, initial=1)) if s < e), sum(a) + 1)


def max_min_window(a: list[int]) -> list[int]:
    """For every window size return the maximum of the minimums."""
    # The idea is to find a window size for each element, where the
    # element is the minimum. Larger elements have smaller window size.
    # This is done by finding the index for the left and right element
    # that is smaller than the current element.
    #
    # Using: [10, 20, 30, 50, 10, 70, 30] as example.

    def bracket(b: list[int], it: Iterable[int]) -> list[int]:
        """Compute the left and right index of a smaller element."""
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


def partition_equal_sum(a: list[int], k: int) -> bool:
    """Partition `a` into `k` subset with equal sum value."""
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


def candy(r: list[int]) -> int:
    """Return a number of candies needed to distribute among children.

    Given ratings `r` reward each kid with candies.
    If a child is better than its neighbor it get more candies.
    Each child gets at least 1 candy.

    Return number of candies needed.
    """
    n = len(r)
    # Start with 0 candies as bottom line for each kid.
    # Accumulate number of candies if rewards are increasing, otherwise reset to 0
    c = accumulate(range(n), lambda a, i: i and r[i] > r[i - 1] and a + 1 or 0)
    # The same in reverse.
    d = accumulate(range(n), lambda a, i: i and r[-i - 1] > r[-i] and a + 1 or 0)
    # Take the maximum of both heaps of candies (and add an extra candy for each kid).
    return sum(max(x, y) for x, y in zip(c, reversed(list(d)))) + n


def max_profit(prices: list[int], k: int) -> int:
    """Return a max-profit for at most `k` sells using `prices` for each day."""
    # Each transaction needs a buy and a sell
    k = min(k, len(prices) // 2)
    # For each transaction count `t`:
    #   - cumulative max profit achievable
    profit = [0] * k
    #   - cumulative max balance = profit for `t-1` transactions minus buy price.
    balance = [-max(prices, default=0)] * k

    for d, p in enumerate(prices):
        # There can be at most d // 2 transactions up until day `d`.
        for t in range(min(1 + d // 2, k)):
            # The idea follows this chain of transformations.
            # Each day we have the choice of two actions:
            #    `noop = profit[d - 1][t]`
            #    `sell = max(p[d] - p[buy] + profit[buy][t - 1] for buy in range(d))`
            # where `sell` can be transformed to:
            #    `sell  = p[d] + max(profit[buy][t - 1] - p[buy] for buy in range(d)))`
            # The second term is the max achievable balance from `t-1` transactions.
            # The `balance` term can be computed as:
            #    `balance[d][t] = max(balance[d-1][t], profit[d][t-1] - p[d])`
            # If we abandon the day `d` in the memo tables:
            #    `balance[t] = max(balance[t], profit[t-1] - p)`
            balance[t] = max(balance[t], (t and profit[t - 1]) - p)
            profit[t] = max(profit[t], p + balance[t])

    return len(profit) and profit[-1] or 0


def count_changes_to_make_strict(a: list) -> int:
    """Count numbers to be changed in `a` to make the sequence strictly increasing."""
    # The idea is to find the longest (non-continuous) increasing subsequence (LIS).
    # The remaining numbers in `a` will need to be changed.
    # In order to do this, we have to make sure that all the remaining numbers
    # can be changed to integers in the intervals between numbers in the LIS.

    @lru_cache(None)
    def lis(j: int) -> int:
        # Uses the longest increasing sequence algorithm.
        #   A. Take maximum (+1) of every LIS in the range [0, j)
        #   B. If there is no such subsequence, return 1 number length by default.
        return max((lis(i) + 1 for i in range(j) if increasing(i, j)), default=1)

    # Define `increasing` as increasing in value
    # with the interval long enough `(j - i)` to accommodate integer numbers in-between.
    increasing = lambda i, j: a[i] < a[j] and (j - i) <= (a[j] - a[i])

    # Number of characters left after removing the longest increasing subsequence.
    return len(a) - max(map(lis, range(len(a))), default=0)


def repeated_numbers(a: list[int]) -> tuple:
    """Return repeated numbers from `a`."""
    # The idea is to mark the numbers as repeated
    # by flipping the sign at their index position.
    # Since the values may become negative, we need to use `abs`

    def repeated(e: int) -> int:
        f = a[abs(e)] = -a[abs(e)]
        return f > 0 and abs(e)

    return tuple(filter(None, map(repeated, a)))


def compress_geek_road(r: list[int], sections: set) -> list[tuple]:
    """Compress the road `r` representation.

    The road is compressed into the following representation:
        (<baggage>, <intersection-value>, <intersection-length>).

    where:
        - baggage is the sum of all values since the last intersection.
        - intersection-value is the number of balls shared between roads.
        - intersection-length is the count of the intersection buckets
            repeating with the same intersection-value.

    Args:
    ----
        r (List[int]): road consisting of counts of balls
        sections (set): counts of balls that mark intersections

    Returns:
    -------
        List(tuple): list of tuples describing intersections
            and values in-between.

    """
    c = []
    i = 0
    while i < len(r):
        b = 0  # baggage collected on the way
        while i < len(r) and r[i] not in sections:
            b += r[i]
            i += 1
        # Intersection value.
        jv = r[i] if i < len(r) else 0
        # Intersection length.
        jc = 0
        while i < len(r) and r[i] == jv:
            jc += 1
            i += 1
        c.append((b, jv, jc))
    return c


def geek_roads(a: list[int], b: list[int]) -> int:
    """Collect the balls stored in buckets on two roads: `a` and `b`.

    Two roads `a` and `b` are given. On each road there are buckets
    with balls, which can be collected when Geek is on that road.

    Geek can switch between roads at intersections marked by the same
    number of balls in a bucket.

    The buckets on each road are sorted in increasing order.

    Return the maximum number of balls that can be collected.

    E.g.:
    For the following roads:
        a: 2 3 5
        b: 1 3 3 4
    The paths taken can be:
        1. 2 3 5 = 10
        2. 1 3 3 4 = 11
        3. 2 3 3 4 = 12
        4. 1 3 3 5 = 12
    The result is 12.
    """
    # Note: As of 2024-04-26 the G4G golden solution was broken.
    # So this will not solve G4G: "Geek Collects Balls" problem
    # if the multiple errors in the verifier logic still exist.

    # Intersecting numbers
    sections = set(a) & set(b)
    if len(sections) == 0:
        # If the roads do not intersect,
        # there are only two path possible.
        return max(sum(a), sum(b))

    # Compress the roads and assure that
    # the compressed representations are of the same length.
    # The compression could be done in-line,
    # but this makes the code easier,
    # as it separates the two aspects and allows
    # for easier debugging.
    lr = compress_geek_road(a, sections)
    rr = compress_geek_road(b, sections)
    if len(lr) < len(rr):
        lr.append((0, 0, 0))
    elif len(rr) < len(lr):
        rr.append((0, 0, 0))
    assert len(lr) == len(rr)  # noqa: S101

    # Sum of the balls on the `a` (left) and `b` (right) roads.
    l = r = 0
    for (lb, v, lil), (rb, rv, ril) in zip(reversed(lr), reversed(rr)):
        # Assert that intersection values are aligned.
        assert v == rv  # noqa: S101
        # Step through or wave in and out.
        # When waving in and out, we sacrifice two 'v' buckets.
        # Waving is only possible if there are at least
        # two buckets on each side.
        c = v if lil < 2 or ril < 2 else v * (lil + ril - 2)
        # When crossing over, only one 'v' bucket is sacrificed.
        x = v * (lil + ril - 1)
        # Update the left and right path sums,
        # choosing the max for continuing on the same road
        # or crossing from the other one.
        l, r = lb + max(l + c, r + x), rb + max(r + c, l + x)

    return max(l, r)


def next_element(p: Callable, a: list[int], default: Any = None) -> list:
    """Return, for elements `e` in `a`, the next one `n` satisfying `p(n, e)`.

    Example
    -------

    ar.next_element(op.gt, [6, 3, 4, 5], -1)
        -> [-1, 4, 5, -1]

    Parameters
    ----------
    p : Callable
        Predicate taking two arguments.
    a : list
        A list of values.
    default: Any
        A value used instead of the next element value
        if no subsequent element can satisfy `p`.

    Returns
    -------
    list
        A list of values indicating the next element satisiying `p`,
        or `default` each time no such element can be found.

    """
    s = []
    o = [default] * len(a)
    for i, e in enumerate(a):
        while s and p(e, a[s[-1]]):
            o[s.pop()] = e
        s.append(i)
    return o


def geeky_132_buildings(b: list[int]) -> bool:
    """Return True if there are 3 building so that: `b[i1] < b[i3] < b[i2]`.

    Finds 3 buildings with indexes `i1 < i2 < i3` such that the middle
    one is larger that the other and the third one is larger than the first.

    Parameters
    ----------
    b : list
        List of buildings' sizes.

    Returns
    -------
    bool
        True if there are 3 buildings fitting the description.

    """
    # Let's declare the indexes of the solution to be: `x, y, z`
    # The idea is to maintain the largest buildings' sizes, so far,
    # on the stack in descending order. The last building's size
    # on the stack is then considered to be `y` - the middle building.
    # At the same time, we assign the largest size, smaller than `y`,
    # popped from the stack to the variable `z`.
    # While iterating in reverse the current element is considered as `x`,
    # and becomes `y` by pushing it onto stack.
    s = []  # `y` values in descending order
    z = 0  # largest element smaller than y = s[-1]
    for x in reversed(b):
        if x < z:  # < y
            return True
        while s and x >= s[-1]:
            z = s.pop()
        s.append(x)  # becomes `y`
    return False
