"Algorithms relating to knapsack and bin-packing problems."

from heapq import nsmallest
from typing import List


def walls_coloring(cost: List[List[int]]) -> int:
    """Given N walls, paint those using K colors, reducing cost from the `cost` matrix.

    The restriction here is that two walls next to each other
    have to be painted differently.

    Args:
        cost (List[List[int]]): NxK cost matrix

    Returns:
        int: the minium cost to paint the walls.
    """
    # Shortcuts:
    if len(cost) == 0 or len(cost[0]) == 0:
        return -1
    if len(cost[0]) == 1:
        # If there is only 1 color, it is impossible to alternate colors between walls.
        return cost[0][0] if len(cost) == 1 else -1

    # This is a knapsack problem and can be solved using dynamic programming.
    # The first idea is to create a `dp[w][p]` matrix and fill it up
    # left-to-right, starting at the left wall. This approach is `O(N*K*K)`.
    # In that approach we calculate the minimum over `dp[w-1][k]` for all
    # values except the one that was used to paint in the previous iteration.
    #
    # An optimization is to realize that `dp[w-1]` contains all the values from
    # the previous pass and the `min(dp[w-1])` is the minimum for the previously
    # chosen color.
    #
    # Thus the solution is to calculate the two smallest numbers form `dp[w-1]`
    # and use those alternatively depending which color was chosen.
    # Given that we only iterate over the walls and then over colors,
    # the time complexity is `O(N*K)`
    # and space required is `O(1)`.

    # Use two smallest numbers (for the firs wall).
    # The `m1` and `m2` variables store (<cost-so-far>, <previous-color>)
    m1, m2 = nsmallest(2, ((cs, c) for c, cs in enumerate(cost[0])))
    # Depending on the current color `c`, choose the minimum value to add.
    # This makes sure that we don't paint walls next to each other with the same color.
    mn = lambda c: m1[0] if m1[1] != c else m2[0]
    for w in range(1, len(cost)):
        # Recalculate the two smallest cost numbers for this wall.
        # `cs + mn(c)` - chooses the cost of the paint, while alternating the colors.
        m1, m2 = nsmallest(2, ((cs + mn(c), c) for c, cs in enumerate(cost[w])))
    # Return the lowest cost.
    return m1[0]
