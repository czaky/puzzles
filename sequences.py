"Utilities handling iterators."

from itertools import islice
from typing import Callable, Iterable


def at(*args):
    "Returns a function that indexes a sequence or a dictionary."

    def index(x):
        for i in args:
            x = x[i]
        return x

    return index


def find_if(
    predicate: Callable,
    iterable: Iterable,
    key: None | Callable = None,
    start: int = 0,
    stop: None | int = None,
    default=None,
):
    """Find an object in `iterable` fulfilling the `predicate`.

    Args:
        predicate (Callable): predicate needs to be true.
        it (Iterable): iterable to search for an object.
        key (Callable, optional): function applied to each object.
        start (int, optional): start position on the iterable. Defaults to 0.
        stop (None | int, optional): stop position (exclusive) on the iterable. Defaults to None.
        default (_type_, optional): Value returned if nothing else is found. Defaults to None.

    Returns:
        Object: the object fulfilling the `predicate` or `default` if not found.
    """
    p: Callable = predicate if not key else lambda x: predicate(key(x))
    it: Iterable = iterable if not (start or stop) else islice(iterable, start, stop)
    return next((x for x in it if p(x)), default)
