"""Search Utils."""

from __future__ import annotations

from typing import Any, Callable


def upper_index(predicate: Callable, l: int, h: int, result: Any = None) -> Any:
    """Return the max index of an element which for which `predicate` is True.

    Search starts between `l` and `h` markers.
    If `predicate` is True, `l` goes up, otherwise `h` goes down.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes index of the element.
    l : int
        lowest index to start search from (inclusive).
    h : int
        highest index to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.

    Returns
    -------
    Any
        The max index of an element which fulfills the predicate.

    """
    while l <= h:
        m = (l + h) // 2
        if predicate(m):
            result = m
            l = m + 1
        else:
            h = m - 1
    return result


def lower_index(predicate: Callable, l: int, h: int, result: Any = None) -> Any:
    """Return the min index of an element which for which `predicate` is True.

    Search starts between `l` and `h` markers.
    If `predicate` is True, `h` goes down, otherwise `l` goes up.
    If `predicate` always returns False, default `result` value is returned.

    Parameters
    ----------
    predicate : Callable
        True for element being searched; takes index of the element.
    l : int
        lowest index to start search from (inclusive).
    h : int
        highest index to start search from (inclusive).
    result : Any, optional
        a value to return by default if no element was found.

    Returns
    -------
    Any
        The max index of an element which fulfills the predicate.

    """
    while l <= h:
        m = (l + h) // 2
        if predicate(m):
            result = m
            h = m - 1
        else:
            l = m + 1
    return result


def largest_sum_cycle(edges: list[int]) -> int:
    """Return the max node index sum of cycles in graph defined by `edges`."""
    # Simplest recursive solution in `O(|E|)`.
    # For each cycle we compute the total path sum reached so far.
    # This allows us to remove any tangling prefix nodes from the sum.
    # At the same time the `edges` are marked as dead-end.
    # This allows the code to run in `O(|E|)`

    # Contains the sums of the paths.
    v = [-1] * len(edges)

    def visit(i: int, s: int) -> int:
        if edges[i] < 0:
            return -1
        s += i
        if v[i] >= 0:
            # Remove any prefix from the sum.
            return s - v[i]
        # Mark the cell with the sum so far.
        v[i] = s
        result = visit(edges[i], s)
        # Mark the cell as dead-end to prevent revisits.
        edges[i] = -1
        return result

    return max(visit(i, 0) for i in range(len(edges)))


def geek_cake_distribution(chunks: list[int], k: int) -> int:
    """Divide a cake into k slices. Return the sweetness of the least sweet slice."""

    def slices(min_sweetness: int) -> int:
        sc = 0  # slices-count
        ss = 0  # slice-sweetness
        for s in chunks:
            ss += s
            if ss >= min_sweetness:
                sc += 1
                ss = 0
        return sc

    return upper_index(lambda m: k <= slices(m), min(chunks), sum(chunks), 0)
