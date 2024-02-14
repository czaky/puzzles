"""Puzzles related to strings."""

from collections import Counter
from typing import List

def reverse_words(s: str, sep: str=' ') -> str:
    "Reverse the order of words in `s`, separated by `sep`."
    return sep.join(reversed(s.split(sep)))

def palindrome(s: str) -> bool:
    "True if `s` is a palindrome."
    # s == s[::-1]
    # Runs in O(N) time and O(1) space.
    return next((False for i in range(len(s)//2) if s[i] != s[-1-i]), True)

def anagram(a: str, b: str) -> bool:
    "True if `a` and `b` contain the same characters."
    return Counter(a) == Counter(b)

def common_prefix(a: List[str]):
    "Return the longest prefix among the strings from `a`."
    if not a:
        return ''
    mnl = min(map(len, a))
    p = next((i for i in range(mnl) for s in a if s[i] != a[0][i]), mnl)
    return a[0][:p]

def equal_rotated(a: str, b: str, n: int) -> bool:
    "True if `a` and `b` are rotated by `n` in any direction."
    n %= min(len(a), len(b))
    return a == b[n:] + b[:n] or b == a[n:] + a[:n]

def first_unique(s: str) -> str:
    "First unique character in the string `s`."
    c = Counter(s)
    return next((x for x in s if c[x]==1), '$')
