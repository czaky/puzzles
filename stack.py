"""Puzzles related to stacks."""

from collections import Counter
from itertools import islice
from typing import Any, Iterable, Iterator, List, Sequence, Set


class StackSet(Sequence, Set):
    """A set that is also a stack. Keeps track of elements' positions."""

    def __init__(self, iterable=()):
        self.stack = list(iterable)
        self.pos = {e: i + 1 for i, e in enumerate(self.stack)}

    def push(self, n):
        "Push `n` onto the stack adding it to the set if not present yet."
        if n not in self.pos:
            self.pos[n] = len(self.stack)
            self.stack.append(n)

    def pop(self, default=None) -> Any:
        "Pop the last element from the stack and remove it from the set."
        if self.stack:
            e = self.stack.pop()
            del self.pos[e]
            return e
        return default

    def top(self, default=None) -> Any:
        "Return the top element of the stack."
        return self.stack[-1] if self.stack else default

    def cut(self, size: int = 0) -> list:
        "Cut the stack to size. Return removed elements."
        if len(self.stack) >= size:
            removed = self.stack[size:]
            del self.stack[size:]
            for e in removed:
                del self.pos[e]
            return removed
        return [][:]

    def clear(self):
        "Remove and return all elements from the stack-set."
        del self.stack[:]
        self.pos.clear()

    def copy(self) -> "StackSet":
        "Return a shallow copy of the stack-set."
        return StackSet(self.stack)

    def count(self, value: object) -> int:
        "Return the count of `value` on the stack."
        return 1 if value in self.pos else 0

    def index(self, value: object, start: int = 0, stop=None) -> int:
        "Index of the first occurence of `value` in the stack."
        return self.pos[value]

    def reverse(self):
        "Reverse the stack."
        self.stack.reverse()

    def extend(self, iterable: Iterable):
        "Extend the stack with an `iterable`."
        for e in iterable:
            self.push(e)

    def __len__(self) -> int:
        return len(self.stack)

    def __bool__(self) -> bool:
        return len(self.stack) > 0

    def __contains__(self, value: object) -> bool:
        return value in self.pos

    def __str__(self) -> str:
        return str(self.stack)

    def __iter__(self) -> Iterator:
        yield from self.stack

    def __reversed__(self) -> Iterator:
        return reversed(self.stack)

    def __getitem__(self, i: int | slice):
        return self.stack[i]

    def __delitem__(self, i: int | slice):
        if isinstance(i, slice):
            for e in self.stack[i]:
                del self.pos[e]
        elif isinstance(i, int):
            del self.pos[self.stack[i]]
        del self.stack[i]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, StackSet) and self.stack == other.stack


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
            if self.counter[e] <= 0:
                del self.counter[e]
            return e
        return default

    def top(self, default=None) -> Any:
        "Return the top element of the stack."
        return self.stack[-1] if self.stack else default

    def cut(self, size) -> List[Any]:
        "Shrink the stack to `size`. Returns cut elements in FIFO order."
        if len(self.stack) > size:
            removed = self.stack[size:]
            del self.stack[size:]
            self.counter.subtract(removed)
            for e in removed:
                if self.counter[e] <= 0:
                    del self.counter[e]
            return removed
        return [][:]

    def clear(self):
        "Remove and return all elements from the stack-set."
        del self.stack[:]
        self.counter.clear()

    def copy(self) -> "CountedStack":
        "Return a shallow copy of the stack-set."
        return CountedStack(self.stack)

    def count(self, value: object) -> int:
        "Return the count of `value` on the stack."
        return self.counter[value]

    def index(self, value: object, start: int = 0, stop=None) -> int:
        "Index of the first occurrence of `value` in the stack."
        if self.counter[value] > 0:
            return self.stack.index(value, start, stop)
        raise ValueError(f"Element '{value}' not found in CountedStack.")

    def reverse(self):
        "Reverse the stack."
        self.stack.reverse()

    def extend(self, iterable: Iterable):
        "Extend the stack with an `iterable`."
        sl = len(self.stack)
        self.stack.extend(iterable)
        self.counter.update(islice(self.stack, sl, None))

    def __len__(self) -> int:
        return len(self.stack)

    def __bool__(self) -> bool:
        return len(self.stack) > 0

    def __iter__(self) -> Iterator:
        yield from self.stack

    def __reversed__(self) -> Iterator:
        return reversed(self.stack)

    def __contains__(self, value: object) -> bool:
        return self.counter[value] > 0

    def __getitem__(self, i: int | slice):
        return self.stack[i]

    def __delitem__(self, i: int | slice):
        if isinstance(i, slice):
            self.counter.subtract(self.stack[i])
            for e in self.stack[i]:
                if self.counter[e] <= 0:
                    del self.counter[e]
        elif isinstance(i, int):
            e = self.stack[i]
            self.counter[e] -= 1
            if self.counter[e] <= 0:
                del self.counter[e]

        del self.stack[i]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CountedStack) and self.stack == other.stack

    def __str__(self) -> str:
        return str(self.stack)
