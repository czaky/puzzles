"""Module for number and arithmetic related puzzles."""

def floor_sqrt(x: int) -> int:
    "Return the floor of `sqrt(x)`."
    if x in (0, 1):
        return x
    l = 0
    h = x
    r = 0
    while l <= h:
        m = (l + h) // 2
        if m*m == x:
            return m
        if m*m < x:
            r = m
            l = m + 1
        else:
            h = m - 1
    return r

def frog_hops(n: int) -> int:
    "In how many ways a frog can cover N tiles when jumping: 1, 2, or 3?"
    ways = [0, 1, 2, 4]
    for i in range(4, n + 1):
        ways[i%4] = ways[(i-1)%4] + ways[(i-2)%4] + ways[(i-3)%4]
    return ways[n%4]

def binary_string_by_three(s: str) -> bool:
    "True if binary number in `s` is divisible by 3."
    # difference of even and odd "1"s is divisible by 3
    return (sum(c == "1" for i, c in enumerate(s) if i%2) -
            sum(c == "1" for i, c in enumerate(s) if i%2 == 0))%3 == 0

def josephus(n: int, k: int) -> int:
    "Return zero-based index of survivor in Josephus problem."
    return (josephus(n-1, k) + k) % n if n > 1 else 0

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
