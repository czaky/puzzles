"""Puzzles related to brackets, parentheses, and braces."""

from __future__ import annotations

from typing import Iterable, Iterator

OPENING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
    "⟨": "⟩",
    "《": "》",
    "⌈": "⌉",
    "⌊": "⌋",
    "【": "】",
    "〖": "〗",
    "⧘": "⧙",
    "⧚": "⧛",
}


def balanced(s: str) -> bool:
    """Check if string `s` brackets are balanced in O(N) space."""
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        elif c in OPENING:
            stack.append(OPENING[c])
        else:
            return False
    return not stack


def max_valid_len(s: str) -> int:
    """Maximum length of a valid parentheses sub-string."""
    # O(1) space; O(N) time
    n = len(s)

    def scan(a: Iterable) -> Iterator:
        ac = i = 0
        for j, e in enumerate(a):
            ac = max(ac, 0) + e
            i = ac < 0 and n or min(i, j)
            if ac == 0:
                yield j - i + 1
        yield 0

    return max(
        *scan(2 * int(c == "(") - 1 for c in s),
        *scan(2 * int(c == ")") - 1 for c in reversed(s)),
    )

def longest_balanced_parenthesis_substring(s: str) -> int:
    """Find the longest substring in `s` with a valid, balanced parentheses.

    Parameters
    ----------
    s : str
        A string that contains only: "()".

    Returns
    -------
    int
        The length of the longest substring with valid parentheses.

    """
    # There is absolutely no need for pushing stack, given that there is only one and
    # the same token pushed and we only need the depth of stack, so this solution
    # uses a counter for this. The idea is to loop over from left (and also from right)
    # while keeping the counter of open parentheses. Each time time counter falls
    # below 0, reset the starting position on the string and the counter to 0.

    def longest(s: Iterable, oc: str = "()") -> int:
        op, cl = oc
        open_count = 0
        mx = 0
        start = -1
        for i, c in enumerate(s):
            if c == op:
                open_count += 1
            elif c == cl:
                open_count -= 1
                if open_count == 0:
                    mx = max(mx, i - start)
                elif open_count < 0:
                    start = i
                    open_count = 0
        return mx

    return max(longest(s), longest(reversed(s), oc=")("))
