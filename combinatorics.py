"""Module for algorithms and puzzles related to combinatorics."""

from __future__ import annotations

import numpy as np

DD = np.longdouble

LOG2_GOLDEN_RATIO = np.log2(1.0 + np.sqrt(5.0, dtype=DD), dtype=DD) - 1.0
LOG2_SQRT5 = np.log2(5.0, dtype=DD) / 2.0


def fib_by_rounding(n: int) -> int:
    """Fibonacci number: `(fib(n-1) + fib(n-2))`."""
    # Rounding formula. Works until n == 88 using (long double = 80bits).
    return round(np.power(2, LOG2_GOLDEN_RATIO * n - LOG2_SQRT5, dtype=DD)) if n else 0


def fib(n: int, m: int = 10**9 + 7) -> int:
    """Return fibonacci number: `(fib(n-1) + fib(n-2)) % m`."""  # noqa: D402
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
