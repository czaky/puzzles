"""Module for sorting algorithms and related puzzles."""

from __future__ import annotations


def selection(a: list[int]) -> None:
    """Sort array `a` using selection sort."""
    # List has two regions: sorted - unsorted
    #  Select the min from unsorted.
    #  Exchange it with the first unsorted item - expanding the sorted array.
    n = len(a)
    for i in range(n - 1):
        j = min(range(i, n), key=lambda j: a[j])
        a[i], a[j] = a[j], a[i]


def bubble(a: list[int]) -> None:
    """Sort array `a` using bubble sort."""
    # Swap two elements until all are in order.
    n = len(a)
    for i in range(1, n):
        swapped = False
        for j in range(n - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break


def insertion(a: list[int]) -> None:
    """Sort array `a` using gnome sort."""
    # Similar to bubble sort,
    # except it walks backwards, moving the whole array.
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def gnome(a: list[int]) -> None:
    """Sort array `a` using gnome sort."""
    # Similar to bubble sort,
    # except it walks up and down in one loop.
    i = 0
    while i < len(a):
        if i == 0 or a[i - 1] <= a[i]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1


def quick(a: list[int], start: int = 0, stop: int | None = None) -> None:
    """Sort array `a` using quick sort on interval [start, stop."""

    def partition(i: int, j: int) -> None:
        # `i` and `j` are inclusive.
        # Divide the array a into two.
        m = i + (i - j) // 2
        # Sort a[i] <= a[m] <= a[j]
        # a[m] - will be the 3-point median.
        if a[m] < a[i]:
            a[m], a[i] = a[i], a[m]
        if a[j] < a[i]:
            a[j], a[i] = a[i], a[j]
        if a[j] < a[m]:
            a[j], a[m] = a[m], a[j]
        p = a[m]
        while True:
            while a[i] < p:
                i += 1
            while p < a[j]:
                j -= 1
            if i >= j:
                return j
            a[i], a[j] = a[j], a[i]

    if stop is None:
        stop = len(a)
    if start < stop - 1:
        pi = partition(start, stop - 1)
        quick(a, start, pi)
        quick(a, pi + 1, stop)


def quick_simple(a: list[int], start: int = 0, stop: int | None = None) -> None:
    """Sort array `a` using quick sort on interval [start, stop)."""
    # Uses simple Lamuto partitioning scheme.

    def partition(low: int, hi: int) -> None:
        # `low` and `high` are inclusive.
        # Divide the array a into two.
        p = a[hi]
        # `low` to `i` is the lower portion.
        i = low
        for j in range(low, hi):
            if a[j] <= p:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    if stop is None:
        stop = len(a)
    if start < stop - 1:
        pi = partition(start, stop - 1)
        quick_simple(a, start, pi)
        quick_simple(a, pi + 1, stop)


def merge(a: list[int], start: int = 0, stop: int | None = None) -> None:
    """Sort array `a` using top-down merge sort."""

    def sort(a: list[int], start: int, stop: int, c: list[int]) -> None:
        if start < stop - 1:
            m = (start + stop) // 2
            # Sort partitions.
            sort(c, start, m, a)
            sort(c, m, stop, a)
            # Merge sorted partitions.
            k, i, j = start, start, m
            while i < m and j < stop:
                if c[i] <= c[j]:
                    a[k] = c[i]
                    i += 1
                else:
                    a[k] = c[j]
                    j += 1
                k += 1
            a[k:stop] = c[i:m] if i < m else c[j:stop]

    sort(a, start, stop or len(a), a[:])

def merge_bottom_up(a: list[int]) -> None:
    """Sort array `a` using bottom-up merge sort."""
    n = len(a)
    w = 1
    b, c = a, a[:]

    while w < n:
        for start in range(0, n, w * 2):
            # Merge sorted partitions.
            m, stop = min(n, start + w), min(n, start + w * 2)
            k, i, j = start, start, m
            while i < m and j < stop:
                if c[i] <= c[j]:
                    b[k] = c[i]
                    i += 1
                else:
                    b[k] = c[j]
                    j += 1
                k += 1
            b[k:stop] = c[i:m] if i < m else c[j:stop]
        b, c = c, b
        w *= 2
    if b != a:
        a[:] = b
