"Puzzles around matrices."

from typing import List, Tuple
from itertools import product, accumulate, combinations
from functools import lru_cache, reduce
from bisect import bisect_right
import numpy as np

import arrays


def make(s: str) -> List[List[int]]:
    "Parse a string into a matrix."
    return [list(map(int, l.split())) for l in s.splitlines()]


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
    for i, j in combinations(range(n), 2):
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
        # Multiplying (i, k) x (k, j) matrices gives: (i, j) matrix.
        # The number of multiplications necessary is: i * k * j
        # For each K we multiply two matrices resulting from recursive calls:
        #   sub(i, k)     => (a[i - 1], a[k])
        #   sub(k + 1, j) => (    a[k], a[j])
        m = lambda k: sub(i, k) + a[i - 1] * a[k] * a[j] + sub(k + 1, j)
        # Determine the optimal split for this range.
        return min(map(m, range(i, j))) if i < j else 0

    return sub(1, len(a) - 1)


A = ord("A")


def optimum_brackets(a: List[int]) -> str:
    """
    Given a list of matrix sizes (a[i] x a[i+1])
    return optimal bracketed multiplication expression
    in the form:  `A(BC)D`
    """

    @lru_cache(None)
    def sub(i: int, j: int) -> Tuple[int, int]:
        # Multiplying (i, k) x (k, j) matrices gives: (i, j) matrix.
        # The number of multiplications necessary is: i * k * j
        # For each K we multiply two matrices resulting from recursive calls:
        #   sub(i, k)     => (a[i - 1], a[k])
        #   sub(k + 1, j) => (    a[k], a[j])
        def split(k):
            return sub(i, k)[0] + a[i - 1] * a[k] * a[j] + sub(k + 1, j)[0], k

        # Determine the optimal split for this range.
        return min(map(split, range(i, j))) if i < j else (0, i)

    def par(i: int, j: int) -> str:
        if i == j:
            return chr(A + i - 1)
        k = sub(i, j)[1]
        a, b = par(i, k), par(k + 1, j)
        return a + (b if len(b) == 1 else f"({b})")

    return par(1, len(a) - 1)


def sudoku(grid: List[List[int]]) -> bool:
    "Fill in the grid and return True if solved."
    rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
    left = []

    def flip(n, i, j):
        v = 1 << n
        rows[i] ^= v
        cols[j] ^= v
        boxes[i // 3 + 3 * (j // 3)] ^= v

    for i, j in product(range(9), repeat=2):
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
    mat = np.array([[1, 1], [1, 0]], dtype=int)
    res = np.array([1, 0], dtype=int)
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
    mat = np.array([[a, b, c], [1, 0, 0], [0, 0, 1]], dtype=int)
    res = np.array([1, 0, 0], dtype=int)
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


def zero_sum_sub_matrix(m: List[List[int]]) -> List[List[int]]:
    "Return the largest sub-matrix of `m` that sums to zero."
    # The idea is borrowed from the 2D Kadane's algorithm.
    # We use top, bottom cutoff to accumulate the values for the columns into an array.
    # Then we apply the `zero_sum_sub_array` above to determine the left and right brackets.
    # Using top, bottom, left, and right we calculate the area,
    # which is used to determine the largest matrix.
    r, c = len(m), len(m[0])
    mx = (0, 0, 0, 0, 0)  # -area, top, left, bottom, right
    for top in range(r):
        a = [0] * c  # cumulative sum of columns from `top` to `bottom` row.
        for bottom in range(top, r):
            mb = m[bottom]
            for k in range(c):
                a[k] += mb[k]
            left, right = arrays.zero_sum_sub_max_interval(a)
            area = (bottom + 1 - top) * (right - left)
            # Sort by area first, then top, lef, bottom, and right.
            mx = min(mx, (-area, top, left, bottom + 1, right))

    # `top` and `left` are inclusive, `bottom` and `right` are exclusive here.
    (area, top, left, bottom, right) = mx
    return [r[left:right] for r in m[top:bottom]] if area else []


def min_points_traverse(grid: List[List[int]]) -> int:
    """Traverse a `grid` with positive and negative numbers representing returns.
    What is the necessary minimum of initial points if the sum of returns
    on the grid traversal path cannot fall below 1?
    The path on the grid can only move down and to the right.
    Starting position is (0, 0). Ending position is (m-1, n-1) for a `m x n` grid.
    """
    m, n = len(grid), len(grid[0])
    # The idea is to start with the end position (m-1, n-1) and calculate
    # each successive position by looking below and to the right.
    # This can be done with only an array representing previous row,
    # and calculating it from the right to left.
    # At each point (i, j) the `v[j]` will contain value below,
    # and `v[j + 1]` is the immediately before calculated value to the right.
    #
    # We initialize the array with 1,
    # which is only important for the position `v[n-1]`.
    # This indicates the minimum points necessary to traverse the grid at the start.
    v = [1] * (n + 1)
    # We add an additional column, which will be always at least
    # the maximum possible points that would be necessary for the traversal.
    # This will allow to do `min(v[n-1], v[n])` without extra code.
    v[-1] = 1 - (n and m and m * n * min(map(min, grid)))
    # We iterate through the grid in reverse order.
    for i, j in product(reversed(range(m)), reversed(range(n))):
        # The `v[j]` for this current row is calculated by taking
        # the minium of the position below (i.e. previous `v[j]`)
        # and the position immediately to the right (i.e this row's `v[j+1]`).
        # We add negative values to the required points budget
        # and make sure that positive values will not lower the budget below 1.
        v[j] = max(min(v[j], v[j + 1]) - grid[i][j], 1)
    # After the iteration the value for the top-left position (0, 0) is in `v[0]`.
    return v[0]
