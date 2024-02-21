"""Puzzles related to strings."""

from collections import Counter
from typing import List
from functools import lru_cache

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
        d += prev * (int(prev >= curr)*2 - 1)
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

def edit_distance(s: str, t: str) -> int:
    "Edit distance between two strings `s` and `t`."
    # The `dp` matrix is |s|x|t| in size.
    # The execution takes O(|s|*|t|) steps.
    @lru_cache(None)
    def dist(i, j):
        return min(
                dist(i-1, j) + 1,
                dist(i, j-1) + 1,
                dist(i-1, j-1) + int(s[i] != t[j])
                ) if min(i,j) >= 0 else abs(i - j)
    return dist(len(s)-1, len(t)-1)

def word_break(s: str, d) -> bool:
    "Can the string `s` be broken in words from dictionary `d`?"
    d = set(d)
    d.add('')
    mx = max(map(len, d))
    @lru_cache(None)
    def rec(sub):
        return sub in d or any(
            sub[:i] in d and rec(sub[i:])
            for i in range(min(mx, len(sub)), 0, -1))
    return rec(s)

def largest_palindrome(s: str) -> str:
    "Return largest palindrome substring from `s`."
    sub = [0, 0]
    n = len(s)
    def is_palindrome(i, even):
        for j in range(min(i, n-i + even -1) + 1):
            a = i-j
            b = i+j - even
            if s[a] != s[b]:
                break
            if sub[1] - sub[0] < b - a:
                sub[:] = [a, b]
    for i in range(1, n):
        is_palindrome(i, even=0)
        is_palindrome(i, even=1)

    return s[sub[0]:sub[1] + 1]
