"""Module for the dynamic programming related puzzles."""

from typing import List, Tuple
from functools import lru_cache


def stack_boxes(dims: List[Tuple[int, int, int]]) -> int:
    "Stack boxes of dimensions `dims` and return max-height. Box dimensions may repeat and rotate."
    # The boxes can be rotated, so each of the dimensions can be used twice in the stack.
    # The idea is to first generate a list of all possible rotated dimensions
    # and then sort it in descending order based on the width x depth.
    # We then run through the stack and for each box, we try to stack
    # other boxes further down the list on top.
    # The stacking options continue recursively and for each box,
    # we choose the maximum choice for a box stacking above.
    #
    # Create a set of possible dimensions.
    s = set()
    for x, y, z in dims:
        # Each original dimension can contribute up to 3 rotations.
        s.add((max(y, z), min(y, z), x))
        s.add((max(x, z), min(x, z), y))
        s.add((max(x, y), min(x, y), z))
    d = sorted(s, reverse=True)

    @lru_cache(None)
    def h(i: int) -> int:
        # Check if box dimensions `j` fits on top o this box dimension `i`.
        fit = lambda j: d[j][0] < d[i][0] and d[j][1] < d[i][1]
        # From all possible stackings above, choose the maximum one.
        return d[i][2] + max(map(h, filter(fit, range(i + 1, len(d)))), default=0)

    # Start with any box in the list and choose the maximum height.
    return max(map(h, range(len(d))), default=0)
