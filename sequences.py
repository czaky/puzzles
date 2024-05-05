"""Utilities handling iterators."""

from __future__ import annotations

from functools import reduce
from itertools import islice, starmap
from operator import indexOf
from typing import Any, Callable, Iterable, MutableSequence, Sequence

from functional import bit


def at(*args: Any) -> Any:
    """Return a function that indexes a sequence or a dictionary."""
    # This is similar to itemgetter, except that in case of multiple indexes,
    # it recursively descends the hierarchy instead of returning a tuple.
    return lambda s: reduce(lambda s, i: s[i], args, s)


def assign(s: MutableSequence, v: Any, i: Any, *indexes: Any) -> Any:
    """Assign value `v` to `s` at the recursive `indexes`.

    For example:
        s = [[1, 2, 3], [4, 5, 6]]

        assign(s, "abc", 0, 2) => "abc"

        s => [[1, 2, "abc"], [4, 5, 6]]

    Returns
    -------
        Value `v`.

    """
    if indexes:
        s = reduce(lambda s, i: s[i], islice(indexes, len(indexes) - 1), s[i])
        i = indexes[-1]
    s[i] = v
    return v


def rindex(a: list, v: Any) -> int:
    """Return the rear index of `v` in `a`."""
    return len(a) - indexOf(reversed(a), v) - 1


def find_if(
    predicate: Callable,
    iterable: Iterable,
    key: None | Callable = None,
    start: int = 0,
    stop: None | int = None,
    default: Any = None,
) -> Any:
    """Find an object in `iterable` fulfilling the `predicate`.

    Parameters
    ----------
    predicate : Callable
        predicate describing the object
    iterable : Iterable
        iterable to search through
    key : None | Callable, optional
        function applied to each object to return key value, by default None
    start : int, optional
        start position on the iterable (inclusive), by default 0
    stop : None | int, optional
        stop position on the iterable (exclusive), by default None
    default : Any, optional
        default value returned if no object found, by default None

    Returns
    -------
    Any
        the searched object or the default value

    """
    p: Callable = predicate if not key else lambda x: predicate(key(x))
    it: Iterable = iterable if not (start or stop) else islice(iterable, start, stop)
    return next((x for x in it if p(x)), default)


def count(
    x: Any,
    iterable: Iterable,
    key: None | Callable = None,
    start: int = 0,
    end: None | int = None,
) -> int:
    """Count occurrence of `x` in the `iterable`.

    Args:
    ----
        x (Object): the object to count.
        iterable (Iterable): iterable providing the objects.
        key (None | Callable, optional): applied on items from the `iterable`.
        start (int, optional): start position on the iterable. Defaults to 0.
        end (None | int, optional): end position (exclusive) on the iterable.

    Returns:
    -------
        int: _description_

    """
    it: Iterable = iterable if not (start or end) else islice(iterable, start, end)
    return sum(bit(x == key(e)) for e in it) if key else sum(bit(x == e) for e in it)


def distance(s1: Sequence, s2: Sequence) -> int:
    """Return the distance between strings `s1` and `s2`."""
    return abs(len(s1) - len(s2)) + sum(starmap(lambda x, y: bit(x != y), zip(s1, s2)))
