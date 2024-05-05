"""Puzzles related to stacks."""

from __future__ import annotations

from collections import Counter
from itertools import islice
from typing import Any, Iterable, Iterator, Sequence, Set


class IndexStack(Sequence, Set):
    """A set that is also a stack. Keeps track of elements' positions."""

    def __init__(self, iterable: Iterable = ()) -> None:
        """Create an IndexStack from `iterable`.

        Parameters
        ----------
        iterable : tuple, optional
            initialization values, by default ()

        """
        self.stack = list(iterable)
        self.pos = {e: i + 1 for i, e in enumerate(self.stack)}

    def push(self, n: Any) -> None:
        """Push `n` onto the stack adding it to the set if not present yet."""
        if n not in self.pos:
            self.pos[n] = len(self.stack)
            self.stack.append(n)

    def pop(self, default: Any = None) -> Any:
        """Pop the last element from the stack and remove it from the set."""
        if self.stack:
            e = self.stack.pop()
            del self.pos[e]
            return e
        return default

    def top(self, default: Any = None) -> Any:
        """Return the top element of the stack."""
        return self.stack[-1] if self.stack else default

    def cut(self, size: int = 0) -> list:
        """Cut the stack to size. Return removed elements."""
        if len(self.stack) >= size:
            removed = self.stack[size:]
            del self.stack[size:]
            for e in removed:
                del self.pos[e]
            return removed
        return [][:]

    def cut_from(self, n: Any) -> list:
        """Cut off the stack down from element `n`. Return removed ones."""
        i = self.pos.get(n)
        return [] if i is None else self.cut(i)

    def clear(self) -> None:
        """Remove and return all elements from the stack-set."""
        del self.stack[:]
        self.pos.clear()

    def copy(self) -> IndexStack:
        """Return a shallow copy of the stack-set."""
        return IndexStack(self.stack)

    def count(self, value: object) -> int:
        """Return the count of `value` on the stack."""
        return 1 if value in self.pos else 0

    def index(self, value: object, start: int = 0, stop: int | None = None) -> int:  # noqa: ARG002
        """Index of the first occurence of `value` in the stack."""
        return self.pos[value]

    def reverse(self) -> None:
        """Reverse the stack."""
        self.stack.reverse()

    def extend(self, iterable: Iterable) -> None:
        """Extend the stack with an `iterable`."""
        for e in iterable:
            self.push(e)

    def __len__(self) -> int:
        """Return the depth of this stack."""
        return len(self.stack)

    def __bool__(self) -> bool:
        """Return True if stack is not empty."""
        return len(self.stack) > 0

    def __contains__(self, value: object) -> bool:
        """Return True if `value` is in the stack."""
        return value in self.pos

    def __str__(self) -> str:
        """Return string representation of the stack."""
        return str(self.stack)

    def __iter__(self) -> Iterator:
        """Iterate over the stack."""
        yield from self.stack

    def __reversed__(self) -> Iterator:
        """Return reversed iterator over the stack."""
        return reversed(self.stack)

    def __getitem__(self, i: int | slice) -> Any:
        """Get an item or a slice of the stack, counting from bottom."""
        return self.stack[i]

    def __delitem__(self, i: int | slice) -> None:
        """Remove an item or a slice from the stack."""
        if isinstance(i, slice):
            for e in self.stack[i]:
                del self.pos[e]
        elif isinstance(i, int):
            del self.pos[self.stack[i]]
        del self.stack[i]

    def __eq__(self, other: object) -> bool:
        """Test if two stacks are equal."""
        return isinstance(other, IndexStack) and self.stack == other.stack


class CountedStack(Sequence):
    """Implementation of a stack, that counts its elements."""

    def __init__(self, it: Iterable = ()) -> None:
        """Initialize the CountedStack from the Iterable.

        Parameters
        ----------
        it : Iterable, optional
            initial contents of the stack, by default ()

        """
        self.stack = list(it)
        self.counter = Counter(self.stack)

    def push(self, e: Any) -> None:
        """Push element `e` onto the stack."""
        self.stack.append(e)
        self.counter[e] += 1

    def pop(self, default: Any = None) -> Any:
        """Pop element `e` from the stack."""
        if self.stack:
            e = self.stack.pop()
            self.counter[e] -= 1
            if self.counter[e] <= 0:
                del self.counter[e]
            return e
        return default

    def top(self, default: Any = None) -> Any:
        """Return the top element of the stack."""
        return self.stack[-1] if self.stack else default

    def cut(self, size: int) -> list[Any]:
        """Shrink the stack to `size`. Returns cut elements in FIFO order."""
        if len(self.stack) > size:
            removed = self.stack[size:]
            del self.stack[size:]
            self.counter.subtract(removed)
            for e in removed:
                if self.counter[e] <= 0:
                    del self.counter[e]
            return removed
        return [][:]

    def clear(self) -> None:
        """Remove and return all elements from the stack-set."""
        del self.stack[:]
        self.counter.clear()

    def copy(self) -> CountedStack:
        """Return a shallow copy of the stack-set."""
        return CountedStack(self.stack)

    def count(self, value: object) -> int:
        """Return the count of `value` on the stack."""
        return self.counter[value]

    def index(self, value: object, start: int = 0, stop: Any = None) -> int:
        """Index of the first occurrence of `value` in the stack."""
        if self.counter[value] > 0:
            return self.stack.index(value, start, stop)
        msg = f"Element '{value}' not found in CountedStack."
        raise ValueError(msg)

    def reverse(self) -> None:
        """Reverse the stack."""
        self.stack.reverse()

    def extend(self, iterable: Iterable) -> None:
        """Extend the stack with an `iterable`."""
        sl = len(self.stack)
        self.stack.extend(iterable)
        self.counter.update(islice(self.stack, sl, None))

    def __len__(self) -> int:
        """Return the depth of this stack."""
        return len(self.stack)

    def __bool__(self) -> bool:
        """Return True if stack is not empty."""
        return len(self.stack) > 0

    def __iter__(self) -> Iterator:
        """Iterate over the stack."""
        yield from self.stack

    def __reversed__(self) -> Iterator:
        """Return reversed iterator over the stack."""
        return reversed(self.stack)

    def __contains__(self, value: object) -> bool:
        """Return True if `value` is in the stack."""
        return self.counter[value] > 0

    def __getitem__(self, i: int | slice) -> Any:
        """Get an item or a slice of the stack, counting from bottom."""
        return self.stack[i]

    def __delitem__(self, i: int | slice) -> None:
        """Remove an item or a slice from the stack."""
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
        """Test if two stacks are equal."""
        return isinstance(other, CountedStack) and self.stack == other.stack

    def __str__(self) -> str:
        """Return string representation of the stack."""
        return str(self.stack)
