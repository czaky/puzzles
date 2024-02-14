"""Puzzles related to strings."""

from collections import Counter
from itertools import islice
from typing import List

def reverse_words(s: str, sep: str=' ') -> str:
    "Reverse the order of words in `s`, separated by `sep`."
    return sep.join(reversed(s.split(sep)))

def palindrome(s: str) -> bool:
    "True if `s` is a palindrome."
    # s == s[::-1]
    # Runs in O(N) time and O(1) space.
    return next((False for i in range(len(s)//2) if s[i] !=s [-1-i]), True)

def anagram(a: str, b: str) -> bool:
    "True if `a` and `b` contain the same characters."
    return Counter(a) == Counter(b)

def common_prefix(a: List[str]):
    "Return the longest prefix among the strings from `a`."
    if not a:
        return ''
    if len(a) == 1:
        return a[0]
    mnl = min(map(len, a))
    first = a[0]
    p = next((i for i in range(mnl) for s in a if s[i] != first[i]), mnl)
    return first[:p]
