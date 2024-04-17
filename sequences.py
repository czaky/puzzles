"Utilities handling iterators."

from itertools import islice, starmap
from typing import Callable, Iterable, Sequence
from functools import reduce

from functional import bit


def at(*args):
    "Returns a function that indexes a sequence or a dictionary."
    return lambda x: reduce(lambda a, i: a[i], args, x)


def find_if(
    predicate: Callable,
    iterable: Iterable,
    key: None | Callable = None,
    start: int = 0,
    end: None | int = None,
    default=None,
):
    """Find an object in `iterable` fulfilling the `predicate`.

    Args:
        predicate (Callable): predicate needs to be true.
        it (Iterable): iterable to search for an object.
        key (Callable, optional): function applied to each object.
        start (int, optional): start position on the iterable. Defaults to 0.
        end (None | int, optional): end position (exclusive) on the iterable. Defaults to None.
        default (_type_, optional): Value returned if nothing else is found. Defaults to None.

    Returns:
        Object: the object fulfilling the `predicate` or `default` if not found.
    """
    p: Callable = predicate if not key else lambda x: predicate(key(x))
    it: Iterable = iterable if not (start or end) else islice(iterable, start, end)
    return next((x for x in it if p(x)), default)


def count(
    x,
    iterable: Iterable,
    key: None | Callable = None,
    start: int = 0,
    end: None | int = None,
) -> int:
    """Count occurrence of `x` in the `iterable`.

    Args:
        x (Object): the object to count.
        iterable (Iterable): iterable providing the objects.
        key (None | Callable, optional): applied on items from the `iterable`. Defaults to None.
        start (int, optional): start position on the iterable. Defaults to 0.
        end (None | int, optional): end position (exclusive) on the iterable. Defaults to None.

    Returns:
        int: _description_
    """
    it: Iterable = iterable if not (start or end) else islice(iterable, start, end)
    return sum(bit(x == key(e)) for e in it) if key else sum(bit(x == e) for e in it)


def distance(s1: Sequence, s2: Sequence) -> int:
    "Return the distance between strings `s1` and `s2`."
    return abs(len(s1) - len(s2)) + sum(starmap(lambda x, y: bit(x != y), zip(s1, s2)))
