"""Module for algorithms and puzzles related to combinatorics."""

from __future__ import annotations

import math

import numpy as np

LOG2_GOLDEN_RATIO = math.log((1.0 + 5.0**0.5) / 2.0, 2)
LOG2_SQRT5 = math.log(5.0**0.5, 2)


def fib_by_rounding(n: int) -> int:
    """Fibonacci number: `(fib(n-1) + fib(n-2))`."""
    if n == 0:
        return 1
    # Rounding formula. Works until n == 70.
    return round(pow(2, LOG2_GOLDEN_RATIO * n - LOG2_SQRT5))


def fib(n: int, m: int = 10**9 + 7) -> int:
    """Fibonacci number: `(fib(n-1) + fib(n-2)) % m`."""
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
    """Number of binary strings of length `n` with 1s separted by 0s.

    Args:
    ----
        n (int): length of the strings
        m (int, optional): Modulus. Defaults to 10**9+7.

    Returns:
    -------
        int: count of strings where 1s are separted by 0s

    """
    return fib(n + 2, m)
