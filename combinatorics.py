"""Module for algorithms and puzzles related to combinatorics."""

from __future__ import annotations

from functools import lru_cache

import numpy as np

DD = np.longdouble

LOG2_GOLDEN_RATIO = np.log2(1.0 + np.sqrt(5.0, dtype=DD), dtype=DD) - 1.0
LOG2_SQRT5 = np.log2(5.0, dtype=DD) / 2.0


def fib_by_rounding(n: int) -> int:
    """Fibonacci number: `(fib(n-1) + fib(n-2))`."""
    # Rounding formula. Exact until n == 88 using (long double = 80bits).
    # Approximate within: 10e-15 of the error/fin(n).
    return round(np.power(2, LOG2_GOLDEN_RATIO * n - LOG2_SQRT5, dtype=DD)) if n else 0


def fib(n: int, m: int = 10**9 + 7) -> int:
    """Return fibonacci number: `(fib(n-1) + fib(n-2)) % m`."""  # noqa: D402
    # Runs in O(log N)
    mat = np.array([[1, 1], [1, 0]], dtype=object)
    res = np.array([1, 0], dtype=object)
    n -= 2
    while n > 0:
        if n & 1:
            res = (res @ mat) % m
        mat = (mat @ mat) % m
        n >>= 1
    return sum(res) % m


def generic_fib(a: int, b: int, c: int, n: int, m: int = 10**9 + 7) -> int:
    """Fibonacci number of the form: `(a * f(n-1) + b * f(n-2) + c) % m`."""
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


def separated_ones(n: int, m: int = 10**9 + 7) -> int:
    """Return number of binary strings of length `n` with 1s separted by 0s.

    Args:
    ----
        n (int): length of the strings
        m (int, optional): Modulus. Defaults to 10**9+7.

    Returns:
    -------
        int: count of strings where 1s are separted by 0s

    """
    return fib(n + 2, m)

def sum_of_456_numbers(x: int, y: int, z: int, mod: int = 10**9 + 7) -> int:
    """Return the sum of numbers having at most x 4s, y 5s, and z 6s digits.

    Example
    -------
    X = Y = Z = 1
    sum = 4 + 5 + 6 + 45 + 54 + 56 + 65 + 46 + 64 + 456 + 465 + 546 + 564 + 645 + 654
        = 3675

    Parameters
    ----------
    x : int
        count of 4s
    y : int
        count of 5s
    z : int
        count of 6s
    mod : int, optional
        modulus for the calculation, by default 10**9 + 7

    Returns
    -------
    int
        sum of numbers with the above described property modulo `mod`.

    """

    @lru_cache(None)
    def f(x: int, y: int, z: int) -> tuple[int, int]:
        """Sum numbers with exact digit counts and the count of such numbers."""
        nonlocal s
        if x + y + z == 0:
            # Initial state.
            return 0, 1

        s1, n1 = f(x - 1, y, z) if x else (0, 0)
        s2, n2 = f(x, y - 1, z) if y else (0, 0)
        s3, n3 = f(x, y, z - 1) if z else (0, 0)

        r = (10 * (s1 + s2 + s3) + 4 * n1 + 5 * n2 + 6 * n3) % mod
        # Update the total sum for counts with *at most* specified digit count.
        s = (s + r) % mod
        return r, (n1 + n2 + n3) % mod

    s = 0
    f(x, y, z)
    return s
