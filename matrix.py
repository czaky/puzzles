"Puzzles around matrices."

from typing import List
from itertools import product, tee, accumulate
from functools import lru_cache, reduce
from bisect import bisect_right
import numpy as np


def at(m, *indexes):
    "Return element of `m` at the specific indexes."
    return reduce(lambda m, i: m[i], indexes, m)


def find_sorted(hay: List[List[int]], needle: int) -> bool:
    "True if `needle` is in the sorted `hay` matrix."
    n = len(hay)
    m = len(hay[0])
    i = n - 1
    j = 0
    while i >= 0 and j < m:
        c = hay[i][j]
        if c < needle:
            j += 1
        elif c > needle:
            i -= 1
        else:
            return True
    return False


def rotate90cc(m: List[List[int]]):
    "Rotate matrix `m` 90deg counter-clockwise."
    # Transpose
    n = len(m)
    for i in range(n):
        for j in range(i, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    # Reverse the rows.
    m.reverse()


def optimum_multiplications(a: List[int]) -> int:
    """
    Given a list of matrix sizes (a[i] x a[i+1])
    return minimum number of operations.
    """

    @lru_cache(None)
    def sub(i, j):
        return int(
            i < j
            and min(
                sub(i, k) + sub(k + 1, j) + a[i - 1] * a[k] * a[j] for k in range(i, j)
            )
        )

    return sub(1, len(a) - 1)


def sudoku(grid: List[List[int]]) -> bool:
    "Fill in the grid and return True if solved."
    rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
    left = []

    def flip(n, i, j):
        v = 1 << n
        rows[i] ^= v
        cols[j] ^= v
        boxes[i // 3 + 3 * (j // 3)] ^= v

    for i, j in product(*tee(range(9))):
        flip(grid[i][j] or left.append((i, j)) or 0, i, j)

    def solve(pos):
        if pos < 0:
            return True
        i, j = left[pos]
        unsafe = rows[i] | cols[j] | boxes[i // 3 + 3 * (j // 3)]
        for n in range(1, 10):
            if unsafe & (1 << n):
                continue
            flip(n, i, j)
            grid[i][j] = n
            if solve(pos - 1):
                return True
            flip(n, i, j)
            grid[i][j] = 0
        return False

    return solve(len(left) - 1)


def sorted_median(m: List[List[int]]) -> int:
    "Return a median of a row-wise sorted matrix."
    mid = (len(m) * len(m[0]) + 1) // 2
    l = min(r[0] for r in m)
    h = max(r[-1] for r in m)
    while l <= h:
        x = (l + h) // 2
        if sum(bisect_right(r, x) for r in m) >= mid:
            h = x - 1
        else:
            l = x + 1
    return l


def fib(n, m):
    "Return `n`th Fibonacci number of the form: `(fib(n-1) + fib(n-2))%m`."
    # Runs in O(log N)
    mat = np.array([[1, 1], [1, 0]])
    res = np.array([1, 0])
    n -= 2
    while n > 0:
        if n & 1:
            res = (res @ mat) % m
        mat = (mat @ mat) % m
        n >>= 1
    return sum(res) % m


def generic_fib(a, b, c, n, m):
    "Return `n`th Fibonacci number of the form: `(a*f(n-1) + b*f(n-2) + c)%m`."
    # Runs in O(log N)
    mat = np.array([[a, b, c], [1, 0, 0], [0, 0, 1]])
    res = np.array([1, 0, 0])
    n -= 2
    while n > 0:
        if n & 1:
            res = (res @ mat) % m
        mat = (mat @ mat) % m
        n >>= 1
    return sum(res) % m


def max_sum_rectangle(m: List[List[int]]) -> int:
    "Return the maximum sum of a sub-matrix of `m`."
    # The idea is to iterate over combinations of rows (top, bottom).
    # Computing a cumulative sum for each of those columns between top and bottom row.
    # Then apply Kedane's algorithm against those cumulative sums.
    # This yields the maximum rectangle sum between top and bottom.
    # The maximum of those rectangle sums is the overall maximum.
    r, c = len(m), len(m[0])
    mx = min(map(min, m))
    ked = lambda a: max(accumulate(a, lambda x, y: max(0, x + y), initial=0))
    for top in range(r):
        a = [0] * c
        for bottom in range(top, r):
            mb = m[bottom]
            for k in range(c):
                a[k] += mb[k]
            mx = max(mx, ked(a))
    return mx if mx > 0 else max(map(max, m))
