"""Search Utils"""

import math
from heapq import heappop, heappush
from typing import Optional, List
from itertools import product
from collections.abc import Callable


def binary(gt: Callable, l: int, h: int, i: Optional[int] = None) -> Optional[int]:
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


def binary_lt(lt: Callable, l: int, h: int, i: Optional[int] = None) -> Optional[int]:
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
    start = (int(0), int(0))
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
    q = [(float(d + g + g), int(0), int(0))]
    m = [[math.inf] * n for _ in grid]
    m[0][0] = d
    while q:
        _, px, py = heappop(q)
        d = m[px][py]
        if px == g and py == g:
            return int(d)
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


def connect_islands(grid: List[List[int]]) -> int:
    "Return the size of the largest island that can be made with just one flip."
    n = len(grid)
    islands = [0, 0]  # index == 0 (empty), index == 1 (unexplored)
    # safe grid access shortcut.
    g = lambda x, y: 0 <= x < n and 0 <= y < n and grid[x][y]
    # offset of adjacent points
    adjacency = ((-1, 0), (0, -1), (1, 0), (0, 1))

    def visit(x: int, y: int) -> int:
        "Visit the island at `(x, y)` and mark it with the island with a counter. Return size."
        if g(x, y) != 1:
            return 0
        # Mark the grid with the index of the island.
        grid[x][y] = len(islands)
        # Visit all the adjacent points. Sum up the size.
        return 1 + sum(visit(x + dx, y + dy) for dx, dy in adjacency)

    # Find the islands on the grid and compute their size.
    for x, y in product(range(n), repeat=2):
        size = visit(x, y)
        if size:
            islands.append(size)

    # For each empty cell on the grid determine the size
    # of a new island if the cell is flipped to 1.
    ms = 0
    for x, y in product(range(n), repeat=2):
        if grid[x][y] == 0:
            # Determine (the set of) adjacent islands.
            adjacent = set(g(x + dx, y + dy) for dx, dy in adjacency)
            # Compute the size of a joined island. Draw maximum.
            ms = max(ms, sum(islands[i] for i in adjacent if i) + 1)

    # If `ms == 0`, then `grid` is one big island.
    return ms or n * n
