"""Puzzles related to brackets, parentheses, and braces."""

OPENING = {
    '(':')', '[':']', '{':'}', '<':'>',
    '⟨':'⟩', '《':'》', '⌈':'⌉', '⌊':'⌋',
    '【':'】', '〖':'〗', '⧘':'⧙', '⧚':'⧛' }

def balanced(s: str) -> bool:
    "Check if string `s` brackets are balanced in O(N) space."
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        elif c in OPENING:
            stack.append(OPENING[c])
        else:
            return False
    return not stack
