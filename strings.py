"""Puzzles related to strings."""

from collections import Counter
from typing import List, Optional
from functools import lru_cache, reduce
from itertools import pairwise, accumulate

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
    ab, ba = {}, {}
    return len(a) == len(b) and all(
        cb == ab.setdefault(ca, cb) and
        ca == ba.setdefault(cb, ca)
        for ca, cb in zip(a, b))

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

def largest_palindrome_dp(s: str) -> str:
    "Return largest palindrome substring from `s`."
    # Uses dynamic programming table. O(N^2)
    n = len(s)
    table = [[False] * n for _ in s]

    for i in range(n-1):
        table[i][i] = True
        table[i][i+1] = s[i] == s[i+1]
    table[n-1][n-1] = True

    mi = mj = 0
    for cl in range(3, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (s[i] == s[j] and table[i + 1][j - 1]):
                table[i][j] = True
                mi, mj = i, j

    # return longest palindrome
    return s[mi:mj+1]

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

def smallest_window_with_all_characters(s: str, p: str) -> Optional[str]:
    "Return the smallest window into `s` containing all the chars in `p`."
    sl = len(s)
    pl = len(p)
    if sl < pl:
        return None
    sc = [0] * 256
    pc = Counter(p)
    z = pl
    i = 0
    mi, mj = 0, sl
    for j, ch in enumerate(s):
        sc[ord(ch)] += 1
        if z > 0:
            z -= int(sc[ord(ch)] <= pc.get(ch, 0))
            if z > 0:
                continue

        while i<=j and sc[ord(s[i])] > pc.get(s[i], 0):
            sc[ord(s[i])] -= 1
            i+=1
        if j - i < mj - mi:
            mi, mj = i, j

    return s[mi:mj+1] if mj < sl else None

def boolean_parentheses(s: str) -> int:
    """
For an expression of the type `T|F&T^F`, consisting of literals `T` and `F`,
and consisting of boolean operators `&` (and), `|` (or), `^` (xor),
count the ways the expression can be parenthesized to generate a true value.
    """
    op = {'&':[1,0], '|':[1,1], '^':[0,1]}
    @lru_cache(None)
    def sub(i, j):
        if i == j - 1:
            return int(s[i] == 'T'), int(s[i] == 'F')
        t, f = 0, 0
        for k in range(i+1, j-1, 2):
            t1, f1  = sub(i, k)
            t2, f2  = sub(k+1, j)
            xor = t1 * f2 + f1 * t2
            m = op[s[k]]
            t +=   m[0] * t1*t2 +   m[1] * xor
            f += (1-m[0])*t1*t2 + (1-m[1])*xor + f1*f2
        return t, f
    return sub(0, len(s))[0]

def alien_alphabet(words):
    "For a sorted list of `words` return the alien alphabet used to sort it."
    chars = set(words[0])
    edges = {}
    for a, b in pairwise(words):
        chars.update(b)
        ca, cb = next((ab for ab in zip(a, b) if ab[0]!=ab[1]), (None, None))
        if ca and cb:
            s = edges.get(ca) or edges.setdefault(ca, set())
            s.add(cb)
    s = []
    v = set()
    def sort(n):
        if not n in v:
            v.add(n)
            any(map(sort, edges.get(n, [])))
            s.append(n)
    any(map(sort, chars))
    return ''.join(reversed(s))

def fix_palindrome(s: str) -> str:
    "Return number of characters to be added to make a string a palindrome."
    @lru_cache(None)
    def count(i, j):
        return int(i<j and (
            count(i+1, j-1)
            if s[i] == s[j]
            else min(count(i+1, j), count(i, j-1)) + 1))
    return count(0, len(s)-1)

def artistic_photo_count(s: str, x: int, y: int) -> int:
    """
String `s` contains a photography set including positions for:
    P - the photographer,
    A - the actor/model,
    B - the backdrop.
A valid photo can be made if the actor is placed between the
photographer and the backdrop.
An artistic photo keeps the (index) distance between each
of them to the inclusive interval [x, y].

Return number of artistic photos.
"""
    l = len(s)-1
    ps = list(accumulate(map(lambda c: int(c=='P'), s)))
    bs = list(accumulate(map(lambda c: int(c=='B'), s)))
    p = lambda i: int(i>=0 and ps[min(i, l)])
    b = lambda i: int(i>=0 and bs[min(i, l)])
    actors = [i for i, c in enumerate(s) if c == 'A' and  x <= i <= l-x]

    pab = sum((p(a-x) - p(a-y-1)) * (b(a+y) - b(a+x-1)) for a in actors)
    bap = sum((b(a-x) - b(a-y-1)) * (p(a+y) - p(a+x-1)) for a in actors)

    return pab + bap
