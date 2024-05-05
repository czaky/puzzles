"""Feature Python compatibility."""

from __future__ import annotations

from itertools import tee
from typing import Iterable, Iterator


# Python 3.10
def pairwise(iterable: Iterable) -> Iterator:
    """pairwise('ABCDEFG') --> AB BC CD DE EF FG."""  # noqa: D402
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
