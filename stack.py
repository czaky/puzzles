"""Puzzles related to stacks."""

from collections import Counter
from typing import Any, Iterable, Iterator, List, Sequence


class CountedStack(Sequence):
    """Implementation of a stack, that counts its elements."""

    def __init__(self, it: Iterable = ()):
        self.stack = list(it)
        self.counter = Counter(self.stack)

    def push(self, e: Any):
        "Push element `e` onto the stack."
        self.stack.append(e)
        self.counter[e] += 1

    def pop(self, default=None) -> Any:
        "Pop element `e` from the stack."
        if self.stack:
            e = self.stack.pop()
            self.counter[e] -= 1
            return e
        return default

    def top(self, default=None) -> Any:
        "Return the top element of the stack."
        return self.stack[-1] if self.stack else default

    def cut(self, size) -> List[Any]:
        "Shortens the stack to `size`. Returns cut elements."
        if len(self.stack) > size:
            removed = self.stack[size:]
            del self.stack[size:]
            self.counter.subtract(removed)
            return removed
        return []

    def __len__(self) -> int:
        return len(self.stack)

    def __bool__(self) -> bool:
        return len(self.stack) > 0

    def __iter__(self) -> Iterator:
        return reversed(self.stack)

    def __reversed__(self) -> Iterator:
        yield from self.stack

    def __contains__(self, value: object) -> bool:
        return self.counter[value] > 0

    def __getitem__(self, i: int | slice):
        return self.stack[i]

    def __delitem__(self, i: int | slice):
        if isinstance(i, slice):
            self.counter.subtract(self.stack[i])
        elif isinstance(i, int):
            self.counter[self.stack[i]] -= 1
        del self.stack[i]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CountedStack) and self.stack == other.stack

    def __str__(self) -> str:
        return str(self.stack)
