"""Puzzles related to strings."""

from collections import Counter
from typing import List, Optional
from functools import lru_cache, reduce
from itertools import accumulate, combinations

from graphs import topological_order
from future import pairwise


def reverse_words(s: str, sep: str = " ") -> str:
    "Reverse the order of words in `s`, separated by `sep`."
    return sep.join(reversed(s.split(sep)))


def palindrome(s: str) -> bool:
    "True if `s` is a palindrome."
    # s == s[::-1]
    # Runs in O(N) time and O(1) space.
    return all(s[i] == s[-1 - i] for i in range(len(s) // 2))


def anagram(a: str, b: str) -> bool:
    "True if `a` and `b` contain the same characters."
    return Counter(a) == Counter(b)


def isomorphic(a: str, b: str) -> bool:
    "True if characters in `a` and `b` can be mapped 1:1 to each other."
    ab, ba = {}, {}
    return len(a) == len(b) and all(
        cb == ab.setdefault(ca, cb) and ca == ba.setdefault(cb, ca)
        for ca, cb in zip(a, b)
    )


def common_prefix(a: List[str]):
    "Return the longest prefix among the strings from `a`."
    if not a:
        return ""
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
    return next((x for x in s if c[x] == 1), "$")


R2D = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_decimal(r: str) -> int:
    "Return the decimal value of the roman literal `r`."
    d = 0
    prev = 0
    for char in r:
        curr = R2D[char]
        d += prev * (int(prev >= curr) * 2 - 1)
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
        return (
            min(
                dist(i - 1, j) + 1,
                dist(i, j - 1) + 1,
                dist(i - 1, j - 1) + int(s[i] != t[j]),
            )
            if min(i, j) >= 0
            else abs(i - j)
        )

    return dist(len(s) - 1, len(t) - 1)


def word_break(s: str, d) -> bool:
    "Can the string `s` be broken in words from dictionary `d`?"
    d = set(d)
    d.add("")
    mx = max(map(len, d))

    @lru_cache(None)
    def rec(sub):
        return sub in d or any(
            sub[:i] in d and rec(sub[i:]) for i in range(min(mx, len(sub)), 0, -1)
        )

    return rec(s)


def longest_palindrome(s: str) -> str:
    "Return longest palindrome substring from `s`."
    # Uses Manacher's algorithm.
    # Runs in O(N)
    n = len(s) * 2
    if n == 0:
        return ""
    lps = [0] * n
    lps[1] = 1  # size of the first palindrome
    c = 1  # center of the outer palindrome (in s*2)
    r = 2  # right border of the outer palindrome (in s*2)
    mxs, mxe = 0, 1  # borders of the largest palindrome (in s)
    for i in range(2, n):
        # Use the mirror length if `i` is between `c` and `r`.
        l = int(i < r and min(lps[2 * c - i], r - i))
        # Try to expand the length (skip filler chars).
        l += (i + l) % 2 + 1
        while l <= i < n - l and s[(i - l) // 2] == s[(i + l) // 2]:
            l += 2
        # Store the value.
        l = lps[i] = l - 1
        # Update the max interval.
        if l > mxe - mxs:
            mxs, mxe = (i - l) // 2, (i + l) // 2
        # If the current palindrome expanded beyond the
        # previous one, replace the old by this one.
        if i + l > r:
            c = i
            r = i + l

    return s[mxs:mxe]


def subsequence_count(s: str, t: str) -> int:
    "Number of times `t` shows in `s` as a loose subsequence."

    @lru_cache(None)
    def sub(i, j):
        return (
            sub(i - 1, j) + int(s[i] == t[j] and sub(i - 1, j - 1))
            if i >= 0 and j >= 0
            else int(j < 0)
        )

    return sub(len(s) - 1, len(t) - 1)


def palindromic_partitions(s: str) -> int:
    "Return the minimum number of cuts to partition `s` into palindromes."

    @lru_cache(None)
    def isp(i, j):
        return i >= j or s[i] == s[j] and isp(i + 1, j - 1)

    n = len(s)
    dp = [0] * n
    for j in range(n):
        dp[j] = int(isp(0, j)) or reduce(
            min, (dp[k] + 1 for k in range(1, j) if isp(k + 1, j)), j + 1
        )

    return (int(n == 0) or dp[n - 1]) - 1


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

        while i <= j and sc[ord(s[i])] > pc.get(s[i], 0):
            sc[ord(s[i])] -= 1
            i += 1
        if j - i < mj - mi:
            mi, mj = i, j

    return s[mi : mj + 1] if mj < sl else None


def boolean_parentheses(s: str) -> int:
    """
    For an expression of the type `T|F&T^F`, consisting of literals `T` and `F`,
    and consisting of boolean operators `&` (and), `|` (or), `^` (xor),
    count the ways the expression can be parenthesized to generate a true value.
    """
    op = {"&": [1, 0], "|": [1, 1], "^": [0, 1]}

    @lru_cache(None)
    def sub(i, j):
        if i == j - 1:
            return int(s[i] == "T"), int(s[i] == "F")
        t, f = 0, 0
        for k in range(i + 1, j - 1, 2):
            t1, f1 = sub(i, k)
            t2, f2 = sub(k + 1, j)
            xor = t1 * f2 + f1 * t2
            m = op[s[k]]
            t += m[0] * t1 * t2 + m[1] * xor
            f += (1 - m[0]) * t1 * t2 + (1 - m[1]) * xor + f1 * f2
        return t, f

    return sub(0, len(s))[0]


def alien_alphabet(words):
    "For a sorted list of `words` return the alien alphabet used to sort it."
    chars = set(words[0])
    edges = {}
    for a, b in pairwise(words):
        chars.update(b)
        ca, cb = next((ab for ab in zip(a, b) if ab[0] != ab[1]), (None, None))
        if ca and cb:
            s = edges.get(ca) or edges.setdefault(ca, set())
            s.add(cb)
    return "".join(topological_order(chars, edges))


def fix_palindrome(s: str) -> int:
    "Return number of characters to be added to make a string a palindrome."

    @lru_cache(None)
    def count(i, j):
        return int(
            i < j
            and (
                count(i + 1, j - 1)
                if s[i] == s[j]
                else min(count(i + 1, j), count(i, j - 1)) + 1
            )
        )

    return count(0, len(s) - 1)


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
    l = len(s) - 1
    ps = list(accumulate(map(lambda c: int(c == "P"), s)))
    bs = list(accumulate(map(lambda c: int(c == "B"), s)))
    p = lambda i: int(i >= 0 and ps[min(i, l)])
    b = lambda i: int(i >= 0 and bs[min(i, l)])
    actors = [i for i, c in enumerate(s) if c == "A" and x <= i <= l - x]

    pab = sum((p(a - x) - p(a - y - 1)) * (b(a + y) - b(a + x - 1)) for a in actors)
    bap = sum((b(a - x) - b(a - y - 1)) * (p(a + y) - p(a + x - 1)) for a in actors)

    return pab + bap


def distinct_subsequence_count(s: str) -> int:
    "Return number of distinct (loose) subsequences in `s`."
    m = {}
    # subsequence is any sequence with any characters removed.
    # E.g.: aba => '' a ab aa b ba aba => 7
    # Each new character doubles the count of subsequences before.
    # If the character is repeated, we deduplicate
    # by subtracting previous count stored in `m`
    return reduce(lambda a, c: (2 * a - m.get(c, 0), m.update({c: a}))[0], s, 1)


def permutations(string: str) -> list:
    "Return a sorted list of permutations of `string`."
    sols = []
    n = len(string)
    s = list(string)

    def rec(i):
        if i >= n:
            sols.append("".join(s))
            return
        rec(i + 1)
        for j in range(i + 1, n):
            s[j], s[i] = s[i], s[j]
            rec(i + 1)
            s[j], s[i] = s[i], s[j]

    rec(0)
    return sorted(sols)


def pattern_match(pattern: str, string: str) -> bool:
    "Match `pattern` containing `*` and `?` to `string`."
    pl = len(pattern)
    sl = len(string)

    p = s = bp = bs = 0

    skip_stars = lambda: next((i for i in range(p, pl) if pattern[i] != "*"), pl)

    while s < sl:
        if p < pl and pattern[p] in ("?", string[s]):
            p += 1
            s += 1
        elif p < pl and pattern[p] == "*":
            bp = p = skip_stars()
            bs = s
        elif bp:
            # backtrack
            p = bp
            s = bs = bs + 1
        else:
            return False

    return skip_stars() == pl


def longest_repeating_substring(s: str) -> str:
    "Return the longest repeating (non-overlapping) substring from `s`."
    # This runs surprisingly faster than the dynamic programming solution.
    # The worst case is O(N^2) but we use two tricks to cut down the problem space.
    n = len(s)
    mx = ""
    for i in range(n - 1):
        # Skip comparing of smaller substrings than already found.
        j = i + len(mx) + 1
        # Abort if the prefix was not found.
        while s[i:j] in s[j:]:
            # Any string s[i:j] here is longer than `mx`.
            mx = s[i:j]
            j += 1

    return mx


def longest_prefix_suffix_length(p: str) -> int:
    "Return the length of the longest proper prefix that is also a suffix."
    # Uses KMP (Knuth Morris Pratt) algorithm. Runs in O(N).
    pi = [0] * len(p)  # the computed PI table
    k = 0  # length of the prefix
    # `k`` increases with every matched letter, but resets after a mismatch.
    # The length that `k` resets is based on the precomputed `pi` table so far.
    # It resets to 0, or resets to longest `k` so that `p[:k+1] == p[q-k:q+1]`.
    for q in range(1, len(p)):
        # find p[:k] where p[k] == p[q]
        while p[k] != p[q]:
            if k == 0:
                break
            # pi[k - 1] = j, where p[:j] == p[k - j:k]
            # resets to length of the self matched prefix-suffix at `k-1`.
            k = pi[k - 1]
        else:
            # p[:k + 1] == p[q - k:q + 1]
            # We have already matched `k-1` plus one character.
            # pi[q] is the length of prefix p[:k] that matched p[q-k:q]
            pi[q] = k = k + 1
    return pi[-1]


def extra_palindrome_chars(s: str) -> int:
    "Returns number of new chars upfront necessary to make `s` a palindrome."
    # Uses KMP (Knuth Morris Pratt) algorithm  to determine the length
    # of the length of the longest prefix of `s` equal to a suffix of
    # the reverse of `s`.
    n = len(s)
    r = s[::-1]
    # `pi[q]` is the length of a suffix of:
    #    "#" + `r[:q]`
    # matching a prefix of `s[:k]`
    pi = [0] * (n + 1)
    k = 0
    for q in range(n):
        while s[k] != r[q]:
            if k == 0:
                break
            k = pi[k - 1]
        else:
            # Using `q+1` to account for the (missing) `#` char.
            pi[q + 1] = k = k + 1
    return n - pi[-1]


def word_wrap(words: List[int], k: int) -> int:
    "Return min sum(extra_spaces**2) for a wrapped text."
    # Runs in O(n*n), aux space O(n)
    n: int = len(words)
    mx: int = n * k**2  # maximum possible result
    dp: List[int] = [0] * (n + 1)  # dynamic programming scratchpad

    # start from the back
    for i in reversed(range(n)):
        e, c = k + 1, mx  # extra spaces, minimum cost so far
        # add more words to the current line
        for j in range(i, n):
            e -= words[j] + 1
            if e < 0:  # if run over the column limit.
                break
            c = min(c, e**2 + dp[j + 1])
        else:
            continue  # final line does not count to extra spaces
        dp[i] = c

    return dp[0]


def sum_string(s: str) -> bool:
    "True if `s` can be split recursively into `a + b = c` substrings."
    # "12243660" -> "12", "24", "36", "60"
    # The idea is to split the string into 3 parts: a + b + remainder
    # Note that: a, b <- b, a + b
    # So the substrings are basically:   `a + b**n`

    def sub(a: int, b: int, s: str) -> bool:
        c, fin, s = str(a + b), not s, s.lstrip("0")
        return fin or s.startswith(c) and sub(b, a + b, s[len(c) :])

    # Once the first string is split, the initial two parts determine the reminder.
    return any(
        sub(int(s[:i]), int(s[i:j]), s[j:])
        for i, j in combinations(range(1, len(s)), 2)
    )
