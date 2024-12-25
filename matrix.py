"""Puzzles around matrices."""

from __future__ import annotations

from bisect import bisect_right
from functools import lru_cache
from itertools import accumulate, combinations

import arrays


def make(s: str) -> list[list[int]]:
    """Parse a string into a matrix."""
    return [list(map(int, l.split())) for l in s.splitlines()]


def find_sorted(hay: list[list[int]], needle: int) -> bool:
    """Return True if `needle` is in the sorted `hay` matrix."""
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


def rotate90cc(m: list[list[int]]) -> None:
    """Rotate matrix `m` 90deg counter-clockwise."""
    # Transpose
    n = len(m)
    for i, j in combinations(range(n), 2):
        m[i][j], m[j][i] = m[j][i], m[i][j]
    # Reverse the rows.
    m.reverse()


def optimum_multiplications(a: list[int]) -> int:
    """Return minimum number of operations for matrices described by `a`.

    Given a list of matrix sizes of (a[i] x a[i+1])
    return minimum number of operations necessary.

    The number of operations differs by the sequence of
    matrix multiplication applied.
    """

    @lru_cache(None)
    def sub(i: int, j: int) -> int:
        # Multiplying (i, k) x (k, j) matrices gives: (i, j) matrix.
        # The number of multiplications necessary is: i * k * j
        # For each K we multiply two matrices resulting from recursive calls:
        #   sub(i, k)     => (a[i - 1], a[k])
        #   sub(k + 1, j) => (    a[k], a[j])
        m = lambda k: sub(i, k) + a[i - 1] * a[k] * a[j] + sub(k + 1, j)
        # Determine the optimal split for this range.
        return min(map(m, range(i, j))) if i < j else 0

    return sub(1, len(a) - 1)

def balloon_coin_popping(a: list[int]) -> int:
    """Return the maximum number of coins that can be gained if popping balloons.

    If a k'th balloon is popped, it will produce a[k-1] * a[k] * a[k+1] coins.
    The `k-1` and `k+1` balloons are then considered adjacent.

    For simplicity assume that there is a balloon with value 1 on each end.

    Parameters
    ----------
    a : list[int]
        A list of balloon values.

    Returns
    -------
    int
        Sum of coins gained by popping each ballooon.

    """
    a = [1, *a, 1]

    @lru_cache(None)
    def sub(i: int, j: int) -> int:
        # Choose the maximum by popping balloons between `(i, j)` - exclusive.
        # Sub-problems also pop balloons between `(i, k)` or `(k, j)`.
        # Finally, multiply by coins in `i`, `k`, `j`.
        return i + 1 < j and max(
            sub(i, k) + a[i] * a[k] * a[j] + sub(k, j) for k in range(i + 1, j)
        )

    return sub(0, len(a) - 1)


A = ord("A")


def optimum_brackets(a: list[int]) -> str:
    """Return optimal bracketed matrix multiplication string, minimizing operation cost.

    Given a list of matrix sizes (a[i] x a[i+1])
    return optimal bracketed multiplication expression
    in the form:  `A(BC)D`.
    """

    @lru_cache(None)
    def sub(i: int, j: int) -> tuple[int, int]:
        # Multiplying (i, k) x (k, j) matrices gives: (i, j) matrix.
        # The number of multiplications necessary is: i * k * j
        # For each K we multiply two matrices resulting from recursive calls:
        #   sub(i, k)     => (a[i - 1], a[k])
        #   sub(k + 1, j) => (    a[k], a[j])
        def split(k: int) -> tuple[int, int]:
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


def sorted_median(m: list[list[int]]) -> int:
    """Return a median of a row-wise sorted matrix."""
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


def max_sum_rectangle(m: list[list[int]]) -> int:
    """Return the maximum sum of a sub-matrix of `m`."""
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


def zero_sum_sub_matrix(m: list[list[int]]) -> list[list[int]]:
    """Return the largest sub-matrix of `m` that sums to zero."""
    # The idea is borrowed from the 2D Kadane's algorithm.
    # We use top, bottom cutoff to accumulate the values for the columns into an array.
    # Then we apply the `zero_sum_sub_array` above
    # to determine the left and right brackets.
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
