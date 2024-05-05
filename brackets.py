"""Puzzles related to brackets, parentheses, and braces."""

from __future__ import annotations

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


def max_valid_len(s: str):
    """Maximum length of a valid parentheses sub-string."""
    # O(1) space; O(N) time
    n = len(s)

    def scan(a):
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
