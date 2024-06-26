"""Module for puzzles woring on an MxN grid."""

from __future__ import annotations

import math
from collections import deque
from heapq import heappop, heappush
from itertools import product

import mathematics


def parse(s: str) -> list:
    """Parse a matrix from string `s`."""
    return [list(map(int, l.split())) for l in s.splitlines() if l]


def dijkstra(grid: list[list[int]]) -> int:
    """Search a path in an NxN grid of costs per cell. Return overall cost."""
    n = len(grid)
    goal = (n - 1, n - 1)
    start = (0, 0)
    v: set[tuple[int, int]] = {start}
    dc = grid[0][0]
    q: list[tuple[int, tuple[int, int]]] = [(dc, start)]
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


def a_star(grid: list[list[int]]) -> int:
    """Search a path in an NxN grid of costs per cell. Return overall cost."""
    n = len(grid)
    g = n - 1
    d: float = grid[0][0]
    q: list[tuple[float, int, int]] = [(float(d + g + g), 0, 0)]
    m = [[math.inf] * n for _ in grid]
    m[0][0] = d
    while q:
        _, i, j = heappop(q)
        d = m[i][j]
        if i == g and j == g:
            return int(d)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            cx, cy = i + dx, j + dy
            if not (0 <= cx < n and 0 <= cy < n):
                continue
            dc = d + grid[cx][cy]
            if m[cx][cy] <= dc:
                continue
            h = dc + g + g - cx - cy
            heappush(q, (h, cx, cy))
            m[cx][cy] = dc
    return -1


def connect_islands(grid: list[list[int]]) -> int:
    """Return the size of the largest island that can be made with just one flip."""
    n = len(grid)
    islands = [0, 0]  # index == 0 (empty), index == 1 (unexplored)
    # safe grid access shortcut.
    g = lambda x, y: 0 <= x < n and 0 <= y < n and grid[x][y]
    # offset of adjacent points
    adjacency = ((-1, 0), (0, -1), (1, 0), (0, 1))

    def visit(x: int, y: int) -> int:
        # Visit the island at `(x, y)` and
        # mark it with the island with a counter.
        # Returns size.
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
            adjacent = {g(x + dx, y + dy) for dx, dy in adjacency}
            # Compute the size of a joined island. Draw maximum.
            ms = max(ms, sum(islands[i] for i in adjacent) + 1)

    # If `ms == 0`, then `grid` is one big island.
    return ms or n * n


def enclosed_islands_count(grid: list[list[int]]) -> int:
    """Return the count of islands of 1s fully enclosed by 0s.

    If an island touches the edge it is not considered fully enclosed.

    Args:
    ----
        grid (List[List[int]]): a grid of 1s and 0s.

    Returns:
    -------
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


def sudoku(grid: list[list[int]]) -> bool:
    """Fill in the grid and return True if solved."""
    rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
    left = []

    def flip(n: int, i: int, j: int) -> None:
        v = 1 << n
        rows[i] ^= v
        cols[j] ^= v
        boxes[i // 3 + 3 * (j // 3)] ^= v

    for i, j in product(range(9), repeat=2):
        flip(grid[i][j] or left.append((i, j)) or 0, i, j)

    def solve(pos: int) -> bool:
        if pos < 0:
            return True
        i, j = left[pos]
        unsafe = rows[i] | cols[j] | boxes[i // 3 + 3 * (j // 3)]
        for n in range(1, 10):
            if unsafe & (1 << n):
                continue
            flip(n, i, j)
            grid[i][j] = n
            if solve(pos - 1):
                return True
            flip(n, i, j)
            grid[i][j] = 0
        return False

    return solve(len(left) - 1)


def grid_path_count(m: int, n: int, mod: int = 10**9 + 7) -> int:
    """Return number of paths from (m,n) down to (0,0) modulo `mod`."""
    # Runs in O(m+n) due to factorial.
    # This is a combinatorial problem.
    # We have `m+n` steps of left or down.
    # Across the `m+n` steps, we need to choose `n` steps down.
    # The `n` steps down have no definite order.
    # The `m` steps left have no definite order.
    # This makes:
    #   ```(m+n)!/m!/n! = binom(m+n, m)```
    # different paths.
    return mathematics.combmod(m + n, m, mod)


def min_points_traverse(grid: list[list[int]]) -> int:
    """Traverse a `grid` with positive and negative numbers representing returns.

    What is the necessary minimum of initial points if the sum of returns
    on the grid traversal path cannot fall below 1?
    The path on the grid can only move down and to the right.
    Starting position is (0, 0). Ending position is (m-1, n-1) for a `m x n` grid.
    """
    m, n = len(grid), len(grid[0])
    # The idea is to start with the end position (m-1, n-1) and calculate
    # each successive position by looking below and to the right.
    # This can be done with only an array representing previous row,
    # and calculating it from the right to left.
    # At each point (i, j) the `v[j]` will contain value below,
    # and `v[j + 1]` is the immediately before calculated value to the right.
    #
    # We initialize the array with 1,
    # which is only important for the position `v[n-1]`.
    # This indicates the minimum points necessary to traverse the grid at the start.
    v = [1] * (n + 1)
    # We add an additional column, which will be always at least
    # the maximum possible points that would be necessary for the traversal.
    # This will allow to do `min(v[n-1], v[n])` without extra code.
    v[-1] = 1 - (n and m and (m * n * min(map(min, grid))))
    # We iterate through the grid in reverse order.
    for i, j in product(reversed(range(m)), reversed(range(n))):
        # The `v[j]` for this current row is calculated by taking
        # the minium of the position below (i.e. previous `v[j]`)
        # and the position immediately to the right (i.e this row's `v[j+1]`).
        # We add negative values to the required points budget
        # and make sure that positive values will not lower the budget below 1.
        v[j] = max(min(v[j], v[j + 1]) - grid[i][j], 1)
    # After the iteration the value for the top-left position (0, 0) is in `v[0]`.
    return v[0]


def grid_exit(g: list[list[int]]) -> tuple[int, int]:
    """Following the rules, return the exit position from the grid.

    Rules:
        1. You start at (0, 0) in the right direction.
        2. If visiting a grid cell with 0, continue in the current direction.
        3. If visiting cell with 1, rotate right, and reset the cell to 0.
    """
    # The only trick used here are the complex numbers.
    n, m = len(g), len(g[0])
    # Splits a complex number into an imaginary and real part.
    ir = lambda c: (int(c.imag), int(c.real))
    p, d, x, y = 0 + 0j, 1 + 0j, 0, 0
    while 0 <= x < m and 0 <= y < n:
        if g[y][x] == 1:
            g[y][x] = 0
            d *= 1j
        p += d
        y, x = ir(p)
    return ir(p - d)


def shortest_path_with_walls_heap(g: list, k: int) -> int:
    """Return the length of the shortest path punching through at most `k` walls.

    Parameters
    ----------
    g : list
        An NxM grid maze with passages marked as 0 and walls as 1.
    k : int
        Max number of walls to punch through.

    Returns
    -------
    int
        Length of a path through the `grid` maze.

    """
    # Surprisingly the heap version is faster than the `deque` version.
    # It is also simpler, with regard to keeping the state.
    # Here we store the path length in the visited array,
    # with unvisited cells having an arbitrary high value: `m*n`.
    # This is a basic Dijkstra's search, with added priority for
    # count of walls that have been punched through.
    n, m = len(g), len(g[0])
    mn = m * n
    v = [[mn] * m for _ in g]
    q: list = [(0, g[0][0], 0, 0)]
    while q:
        ln, w, px, py = heappop(q)
        if ln > v[px][py]:
            # This happens if a new, better path was found below.
            # This check speeds things up by 50%
            continue
        if px == n - 1 and py == m - 1:
            # After checking for optimality, return the path length.
            return ln
        v[px][py] = ln
        ln += 1
        for x, y in ((px - 1, py), (px + 1, py), (px, py - 1), (px, py + 1)):
            # Only replace the solution so far, if it is better and
            # it did not go over the wall punch limit.
            if 0 <= x < n and 0 <= y < m and v[x][y] > ln and w + g[x][y] <= k:
                v[x][y] = ln
                # States are sorted by path length and by the count of walls.
                heappush(q, (ln, w + g[x][y], x, y))
    return -1


def shortest_path_with_walls_bfs(g: list, k: int) -> int:
    """Return the length of the shortest path punching through at most `k` walls.

    Parameters
    ----------
    g : list
        An NxM grid maze with passages marked as 0 and walls as 1.
    k : int
        Max number of walls to punch through.

    Returns
    -------
    int
        Length of a path through the `grid` maze.

    """
    # Surprisingly the heap version is faster than this `deque` version.
    # Here we store the corresponding search state in the visited array,
    # with unvisited cells having an arbitrary high value: `(m*n, ...)`.
    # This is a basic BFS search, with visited property, being decided
    # by the path length so far and by the walls punched count.
    n, m = len(g), len(g[0])
    mn = m * n
    v: list[list[tuple]] = [[(mn,)] * m for _ in g]
    q: deque[tuple] = deque([(0, g[0][0], 0, 0)])
    while q:
        pv = ln, w, i, j = q.popleft()
        if pv > v[i][j]:
            # This happens, if the `pv` node was replaced below.
            # The check speeds things up 3 times.
            continue
        if i == n - 1 and j == m - 1:
            # Return `ln`, after checking that it is the best path above.
            return ln
        v[i][j] = pv
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < n and 0 <= y < m:
                nv = (ln + 1, w + g[x][y], x, y)
                # Override the node only if it was:
                #   1.) Unvisited: `v[x][y] == (mn,)` or
                #   2.) Costlier: length and walls count higher.
                if v[x][y] > nv and nv[1] <= k:
                    v[x][y] = nv
                    q.append(nv)
    return -1
