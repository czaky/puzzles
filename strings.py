"""Puzzles related to strings."""

from collections import Counter
from typing import List
from functools import lru_cache, reduce

def reverse_words(s: str, sep: str=' ') -> str:
    "Reverse the order of words in `s`, separated by `sep`."
    return sep.join(reversed(s.split(sep)))

def palindrome(s: str) -> bool:
    "True if `s` is a palindrome."
    # s == s[::-1]
    # Runs in O(N) time and O(1) space.
    return all(s[i] == s[-1-i] for i in range(len(s)//2))

def anagram(a: str, b: str) -> bool:
    "True if `a` and `b` contain the same characters."
    return Counter(a) == Counter(b)

def isomorphic(a: str, b: str) -> bool:
    "True if characters in `a` and `b` can be mapped 1:1 to each other."
    if len(a) != len(b):
        return False
    ab = dict(zip(a, b))
    ba = dict(zip(b, a))
    return all(ab[x] == y and ba[y] == x for x, y in zip(a, b))

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
        r = min(i, n-i + even -1)
        if r*2 - even < sub[1] - sub[0]:
            return
        for j in range(1, r+1):
            a = i-j
            b = i+j - even
            if s[a] != s[b]:
                break
            if sub[1] - sub[0] < b - a:
                sub[:] = [a, b]
    m = n//2
    for i in range(1, m + 1):
        is_palindrome(m - i, even=0)
        is_palindrome(m - i, even=1)
        is_palindrome(m + i -1, even=0)
        is_palindrome(m + i -1, even=1)

    return s[sub[0]:sub[1] + 1]

def subsequence_count(s: str, t: str) -> int:
    "Number of times `t` shows in `s` as a loose subsequence."
    @lru_cache(None)
    def sub(i, j):
        return (sub(i-1, j) + int(s[i] == t[j] and sub(i-1, j-1))
                if i >= 0 and j >= 0 else int(j < 0))
    return sub(len(s)-1, len(t)-1)

def palindromic_partitions(s: str) -> int:
    "Return the minimum number of cuts to partition `s` into palindromes."
    @lru_cache(None)
    def isp(i, j):
        return i>=j or s[i] == s[j] and isp(i+1, j-1)

    n = len(s)
    dp = [0] * n
    for j in range(n):
        dp[j] = int(isp(0, j)) or reduce(
            min, (dp[k] + 1 for k in range(1,j) if isp(k+1, j)), j+1)

    return (int(n==0) or dp[n-1]) -1
