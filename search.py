"""Search Utils"""

import math
from collections.abc import Callable
from heapq import heappop, heappush
from itertools import product
from typing import List, Optional


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
            ms = max(ms, sum(islands[i] for i in adjacent) + 1)

    # If `ms == 0`, then `grid` is one big island.
    return ms or n * n


def enclosed_islands_count(grid: List[List[int]]) -> int:
    """Return the count of islands of 1s fully enclosed by 0s.

    If an island touches the edge it is not considered fully enclosed.

    Args:
        grid (List[List[int]]): a grid of 1s and 0s.

    Returns:
        int: count of fully enclosed islands.
    """
    n, m = len(grid), len(grid[0])

    # Idea is to do a graph DFS and mark the grid points as visited.
    # This way we determine each point as belonging to an island.
    # The DFS functions returns 3 values:
    #    0 - no new island,
    #    1 - new fully enclosed island,
    #    2 - new island touching an edge.
    # The function below takes a `max` of the values.

    def v(x: int, y: int) -> int:
        # Check if (x, y) is valid and that it is an unexplored point.
        if not (0 <= x < n and 0 <= y < m and grid[x][y] == 1):
            return 0
        grid[x][y] = 0
        # Determine if this point touches the edge (=> 2)
        t = 2 - (0 < x < n - 1 and 0 < y < m - 1)
        # Visit all the adjacent points.
        # Return 2 for an island touching the edge, 1 otherwise.
        return max(t, v(x + 1, y), v(x - 1, y), v(x, y + 1), v(x, y - 1))

    # Sum only islands that are new and fully enclosed by 0s.
    return sum(v(x, y) == 1 for x, y in product(range(n), range(m)))


def largest_sum_cycle(edges: List[int]) -> int:
    "Return the max node index sum of cycles in graph defined by `edges`."
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
