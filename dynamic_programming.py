"""Module for the dynamic programming related puzzles."""

from collections import Counter
from functools import lru_cache
from typing import List, Tuple


def stack_boxes(dims: List[Tuple[int, int, int]]) -> int:
    """Stack boxes of dimensions `dims` and return the max possible height.
    Box dimensions may repeat and rotate."""
    # The boxes can be rotated, so each of the dimensions
    # can be used twice in the stack.
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


PRIMES_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
PRIMES_10_BITS = 1 << len(PRIMES_10)
PRIMES_10_MASKS = [
    (i % 4 and i % 9 and i % 25)
    and sum(1 << j for j, p in enumerate(PRIMES_10) if not i % p)
    for i in range(31)
]


def prime_product_subset_count(a: List[int], mod: int = 10**9 + 7) -> int:
    """
    Given array `a` count the number of subsets of `a`,
    for which the product consist of distinct primes from 2 to 29.

    Parameters
    ----------
    a : List[int]
        A list of numbers from 1 to 30 (inclusive)
    mod : int
        A modulo value. Defaults to: 10**9 + 7

    Returns
    -------
    int
        Number of subsets with product of only distinct primes.
    """
    # The idea is to use DP, computing the counts of subsets,
    # for each prime combination represented by a bit mask.
    # The array `a` of integers is translated to a bit mask of
    # prime indexes.
    # Then each subset count `dp[j | mask]` is incremented
    # by the count of subsets without the new
    # primes in the number (j & mask != 0) multiplied by the count
    # of the number in the `a` array.
    mcs = tuple(Counter(PRIMES_10_MASKS[e] for e in a).items())
    # Initialize with 1, which is only important for `dp[0]`.
    dp = [1] * (1 << len(PRIMES_10))
    # Build the `dp` array iteratively.
    # `dp[j]` is the sum of all previously encountered sets
    # without the specific mask (of prime factor)
    # multiplied by the counter of numbers with the specific mask.
    # The condition after `if` make sure that
    # `j` is a proper superset of `j ^ mask`.
    # And it makes sure, that we don't count symmetric subsets
    # twice: `j ^ m < m`.
    for j in range(1, len(dp)):
        dp[j] = sum(dp[j ^ m] * c % mod for m, c in mcs if j ^ m < m == j & m)
    return (sum(dp) - 1) * 2 ** a.count(1)
