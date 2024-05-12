"""Module for algorithms and puzzles that use branch and bound approach."""

from __future__ import annotations

import bits


def tsp(cost: list[list[int]]) -> int:
    """Return the exact minimum path cost of the traveling salesman problem.

    The solution will visit all cities in a closed cycle.

    Parameters
    ----------
    cost : list
        Square adjacency matrix describing cost between the nodes.

    Returns
    -------
    int
        Minimum cost to visit all cities using paths from the `cost` matrix.

    """
    # DFS approach using a stack to arrive at
    # proper bounds as fast as possible.
    # Stack seems to be twice as fast as a heap solution.

    n = len(cost)
    if n < 2:
        return 0

    # Used for the lower bound estimation.
    min_out = [min(cost[i][j] for j in range(n) if j != i) for i in range(n)]

    # The resulting minimum path cost.
    mn: int = sum(max(cost[i][j] for j in range(n)) for i in range(n))
    # Stack containing traversal states.
    # lower-bound, cost, unvisited, node-index
    s: list[tuple] = [(sum(min_out), 0, (1 << n) - 2, 0)]

    while s:
        h, c, unvisited, u = s.pop()
        if unvisited == 0:
            mn = min(mn, c + cost[u][0])
            continue
        # Cut by the best solution as early as possible.
        if h >= mn:
            continue
        h -= min_out[u]
        # Iterate over the unvisited node indexes.
        for i, b in bits.enum(unvisited):
            ih = h + cost[u][i]
            # Cut by the best solution found so far.
            if ih < mn:
                s.append((ih, c + cost[u][i], unvisited & ~b, i))

    return mn
