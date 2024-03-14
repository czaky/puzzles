"""Search Utils"""

import math
from heapq import heappop, heappush
from typing import Optional, List
from collections.abc import Callable


def binary(gt: Callable, l: int, h: int, i: int = None) -> Optional[int]:
    """
    Returns the index of an element which is NOT greater than (`gt`).

    Arguments:
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


def binary_lt(lt: Callable, l: int, h: int, i: int = None) -> Optional[int]:
    """
    Returns the index of an element which is NOT less than (`lt`).

    Arguments:
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


def dijkstra_grid(grid: List[List[int]]) -> int:
    "Search a path in an NxN grid of costs per cell. Return overall cost."
    n = len(grid)
    goal = (n - 1, n - 1)
    start = (0, 0)
    v = set([start])
    dc = grid[0][0]
    q = [(dc, start)]
    while q:
        d, p = heappop(q)
        if p == goal:
            return d
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            c = (p[0] + dx, p[1] + dy)
            if not (0 <= c[0] < n and 0 <= c[1] < n) or c in v:
                continue
            v.add(c)
            dc = d + grid[c[0]][c[1]]
            heappush(q, (dc, c))
    return -1


def a_star_grid(grid: List[List[int]]) -> int:
    "Search a path in an NxN grid of costs per cell. Return overall cost."
    n = len(grid)
    g = n - 1
    d = grid[0][0]
    q = [(d + g + g, 0, 0)]
    m = [[math.inf] * n for _ in grid]
    m[0][0] = d
    while q:
        _, px, py = heappop(q)
        d = m[px][py]
        if px == g and py == g:
            return d
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            cx, cy = px + dx, py + dy
            if not (0 <= cx < n and 0 <= cy < n):
                continue
            dc = d + grid[cx][cy]
            if m[cx][cy] <= dc:
                continue
            h = dc + g + g - cx - cy
            heappush(q, (h, cx, cy))
            m[cx][cy] = dc
    return -1
