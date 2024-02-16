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

def isomorphic(a: str, b: str) -> bool:
    "True if characters in `a` and `b` can be mapped 1:1 to each other."
    if len(a) != len(b):
        return False
    ab = dict(zip(a, b))
    ba = dict(zip(b, a))
    return next(
        (False for x, y in zip(a, b) if ab[x] != y or ba[y] != x), True)

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

R2D = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman_to_decimal(r: str) -> int:
    "Return the decimal value of the roman literal `r`."
    d = 0
    prev = 0
    for char in r:
        curr = R2D[char]
        d += prev if prev >= curr else -prev
        prev = curr
    return d + prev

def max_distinct_char_substring(s: str) -> int:
    "Returns length of the longest substring with distinct characters."
    seen = {}
    i = -1
    x = 0
    for j, c in enumerate(s):
        i = max(i, seen.get(c, i))
        x = max(x, j - i)
        seen[c] = j
    return x
