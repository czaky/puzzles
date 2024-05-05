"""Search Utils."""

from __future__ import annotations

from typing import Callable


def binary(gt: Callable, l: int, h: int, i: int | None = None):
    """Returns the index of an element which is NOT greater than (`gt`).

    Arguments:
    ---------
        gt  - greater than predicate; takes index of the element.
        l   - lowest index to start search from (inclusive).
        h   - highest index to start search from (inclusive).
        i   - default index to return (`None` by default).

    """
    while l <= h:
        m = (l + h) // 2
        if gt(m):
            h = m - 1
        else:
            i = m
            l = m + 1
    return i


def binary_lt(lt: Callable, l: int, h: int, i: int | None = None):
    """Returns the index of an element which is NOT less than (`lt`).

    Arguments:
    ---------
        lt  - less than predicate; takes index of the element.
        l   - lowest index to start search from (inclusive).
        h   - highest index to start search from (inclusive).
        i   - default index to return (`None` by default).

    """
    while l <= h:
        m = (l + h) // 2
        if lt(m):
            l = m + 1
        else:
            i = m
            h = m - 1
    return i


def largest_sum_cycle(edges: list[int]) -> int:
    """Return the max node index sum of cycles in graph defined by `edges`."""
    # Simplest recursive solution in `O(|E|)`.
    # For each cycle we compute the total path sum reached so far.
    # This allows us to remove any tangling prefix nodes from the sum.
    # At the same time the `edges` are marked as dead-end.
    # This allows the code to run in `O(|E|)`

    # Contains the sums of the paths.
    v = [-1] * len(edges)

    def visit(i: int, s: int):
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
    """Divide the cake into k + 1 slices. Return the sweetness of the least sweet slice."""

    def slices(min_sweetness: int) -> int:
        sc = 0  # slices-count
        ss = 0  # slice-sweetness
        for s in chunks:
            ss += s
            if ss >= min_sweetness:
                sc += 1
                ss = 0
        return sc

    return binary(lambda m: k > slices(m), min(chunks), sum(chunks), 0) or 0
