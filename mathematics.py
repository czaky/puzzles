"""Module for number and arithmetic related puzzles."""

from math import floor, log
from functools import reduce
from operator import mul


def floor_sqrt(x: int) -> int:
    "Return the floor of `sqrt(x)`."
    if x in (0, 1):
        return x
    l = 0
    h = x
    r = 0
    while l <= h:
        m = (l + h) // 2
        if m * m == x:
            return m
        if m * m < x:
            r = m
            l = m + 1
        else:
            h = m - 1
    return r


def binary_string_by_three(s: str) -> bool:
    "True if binary number in `s` is divisible by 3."
    # difference of even and odd "1"s is divisible by 3
    return (
        sum(c == "1" for i, c in enumerate(s) if i % 2)
        - sum(c == "1" for i, c in enumerate(s) if i % 2 == 0)
    ) % 3 == 0


def josephus(n: int, k: int) -> int:
    "Return zero-based index of survivor in Josephus problem."
    return (josephus(n - 1, k) + k) % n if n > 1 else 0


def factorial_trailing_zeros(n: int) -> int:
    "Returns number of trailing zeros in a factorial of `n`."
    # Zeros come from 5 * 2.
    # Count only 5s as there will be more 2s.
    # 1! to 24! has n // 5 fives as factor.
    # 25! to 124! has 2 * n // 5 fives as factor.
    # ...
    c = 0
    j = 5
    while j <= n:
        c += n // j
        j *= 5
    return c


def paths_in_matrix(m: int, n: int) -> int:
    "Return number of unique paths from (1,1) to (m,n)."
    # (m+n-2)! / (m-1)! / (n-1)!
    return reduce(mul, range(m, m + n - 1), 1) // reduce(mul, range(2, n), 1)


def frog_hops(n: int) -> int:
    "In how many ways a frog can cover N tiles when jumping: 1, 2, or 3?"
    if n == 0:
        return 0
    a, b, c = 1, 1, 2
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a


def uniform_integers(a: int, b: int) -> int:
    """
    Count number of integers between `[a, b]` with same digits.

    Uniform integers are of the form: 111, 222, ..., 999.
    They are made of the same digit in decimal notation.
    """

    def uniform(n):
        l = floor(log(max(n, 1), 10)) + 1
        return 9 * (l - 1) + n // ((10**l - 1) // 9)

    return uniform(b) - uniform(a - 1)


def closest_palindrome_number(n: int) -> int:
    "Return the closest number to `n` that is a palindrome number."
    if n <= 10:
        # Return num if n <= 9
        # Return 9 if n == 10
        return n - n // 10

    def pal(n: int):
        # Create a palindrome number out of `n`.
        s = str(n)
        m, r = divmod(len(s) - 1, 2)
        # For odd lengths the prefix is shorter than suffix.
        return int(s[: m + r] + s[m::-1])

    # Manipulate the middle digit, to cover all cases.
    d = 10 ** int((log(n, 10) + 1) // 2)
    return min(map(pal, (n - d, n, n + d)), key=lambda p: abs(n - p))
