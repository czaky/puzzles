"""Module for number and arithmetic related puzzles."""

from functools import reduce
from math import comb, floor, log
from operator import mul
from typing import Tuple

# The modulo operation is crucial to efficiently solving the division problem.
M = 10**9 + 7


def digits(n: int):
    "Iterates over decimal digits of `n`."
    while n:
        yield n % 10
        n //= 10


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


def next_happy_number(n: int) -> int:
    "The next number to `n` with digits summing to 1 recursively."
    # Get the recursive sum of digits.
    ss = lambda n: n if n < 10 else ss(sum(d * d for d in digits(n)))
    # Recursively determine the next "happy" number.
    nh = lambda n: n if ss(n) in (1, 7) else nh(n + 1)
    return nh(n + 1)


# Caches the table of integers in `range(3, n + 1, 2)`
# Composite numbers in this table are replaced with 0.
_prime_table = []


def _primes(n: int):
    # Generate potential prime numbers skipping all even ones.
    global _prime_table  # pylint: disable=global-statement
    pt = _prime_table
    lpt = len(pt)
    if n - 2 <= lpt:
        return pt

    nums = list(range(3, n + 1, 2))
    nums[: len(pt)] = pt

    # Iterate over all the numbers deemed not composite, yet.
    for p in (p for p in nums if p and p * p <= n):
        # Delete all: p^2, p^2 + p, ... numbers as composite.
        st = (p * p - 3) // 2
        st = st if lpt < st else lpt - (lpt - st) % p
        for i in range(st, len(nums), p):
            nums[i] = 0

    if len(nums) > len(_prime_table):
        _prime_table = nums
    return nums


def prime_numbers(n: int):
    "Generate primes until n."
    if n < 2:
        return
    yield 2
    for p in _primes(n):
        if p > n:
            break
        if p > 0:
            yield p


def prime_sum(n: int) -> Tuple[int, int]:  # pyright: ignore
    "Return two prime numbers that sum to the even number `n`."
    assert n > 3

    primes = list(prime_numbers(n))

    j = len(primes) - 1
    for i, a in enumerate(primes):
        if i > j:
            break
        b = n - a
        while primes[j] > b:
            j -= 1
        if primes[j] == b:
            return a, b

    return 0, n


def best_numbers(n: int, a: int, b: int, c: int, d: int) -> int:
    """Return a count of integers of `n` length of decimal representation that fulfill:
    1.) The numbers are made only of digits `a` and `b`.
    2.) Sum of the digits of the numbers contains at least one of `c` and `d`.
    """
    # The idea is to find `n_a` and `n_b` split with the sum having the property 2.)
    # Then return the number of permutations.

    # A valid number (sum) contains `c` and `d` in the decimal representation.
    cd = set([c, d])
    valid = lambda s: bool(cd & set(digits(s)))

    if a == b:
        # If the digit sum of the `aaa...aaa` number intersects with `cd`,
        # then there is just one hit, else 0.
        return int(valid(a * n))

    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % M

    # Modulo inverse of a number is a number that:
    #  inv(n) * n = n^(M - 2) * n = 1  (mod M)
    # Inverse of the factorial uses the inductive property:
    #  (f_n) ^ (M - 2) * f_n = 1
    #  (f_n-1 * n) ^ (M - 2) * f_n = 1
    #  (f_n-1) ^ (M - 2) * n ^ (M - 2) * f_n = 1
    # So:
    #  (f_n-1) ^ (M - 2)
    #   = 1 / n ^ (M - 2) / f_n
    #   = n / f_n
    #   = n * (f_n) ^ (M - 2)
    # So:
    #  inv(f_n-1) = n * inv(f_n)
    inv = [1] * (n + 1)
    inv[-1] = pow(fac[-1], (M - 2), M)
    for i in reversed(range(1, n + 1)):
        inv[i - 1] = i * inv[i] % M

    # Count of valid combinations for a number consisting of i a's and (n - i) b's.
    p = lambda i: fac[n] * inv[i] * inv[n - i] % M if valid(a * i + b * (n - i)) else 0
    return sum(map(p, range(n + 1))) % M


def find_nth_k_bit_number(n: int, k: int) -> int:
    "Find the `n`th number that has at most `k` bits."
    # The puzzle requires combinatorics, bit-manipulations, and binary-search.
    # The idea is to use binary search, while calculating.
    # the count of numbers for a given speculated solution.

    def k_bit_count(n: int, k: int) -> int:
        # Count of numbers below or equal to `n` with exactly `k` bits.
        if k == 0:
            return 1  # There is only one number with 0 bits.
        m = n.bit_length()
        if m < k:
            return 0  # Cannot have `k` bits in `m < k` bit number.

        # Number of combinations o `k` set bits in `m - 1` length number.
        # Remaining `k - 1` numbers, after discarding the highest bit.
        # For example (n = 25 (11001), k = 4):
        #    Numbers & 1111 = C(4, 4) = 1
        #    Numbers between 1|0000 ... 1|1001 = k_bit_count(1001, 4 - 3)
        return comb(m - 1, k) + k_bit_count(n ^ (1 << m - 1), k - 1)

    # Sum all the combinations for k-bits from 0 to `k`.
    at_most_k_bit_count = lambda n: sum(k_bit_count(n, j) for j in range(k + 1))

    # Determine starting low and high markers.
    l, h = 0, n
    while at_most_k_bit_count(h) < n:
        l, h = h, h + h

    # Binary search.
    while l < h:
        m = (l + h) // 2
        if at_most_k_bit_count(m) >= n:
            h = m
        else:
            l = m + 1
    return l


def combmod(n: int, k: int, mod: int) -> int:
    "Return binominal, combinatorial factor modulo `mod`"
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    g = lambda a, x: a * x % mod
    fk = reduce(g, range(1, k + 1), 1)
    fn = reduce(g, range(n - k + 1, n + 1), 1)
    return fn * pow(fk, -1, mod) % mod
