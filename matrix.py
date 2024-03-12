"Puzzles around matrices."

from typing import List
from itertools import product, tee
from functools import lru_cache, reduce
from bisect import bisect_right


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
