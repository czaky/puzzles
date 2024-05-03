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


def prime_product_subset_count(a: List[int], m: int = 10**9 + 7) -> int:
    """
    Given array `a` count the number of subsets of `a`,
    for which the product consist of distinct primes from 2 to 29.

    Parameters
    ----------
    a : List[int]
        A list of numbers from 1 to 30 (inclusive)
    m : int
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
    counts = Counter(a)
    dp = [0] * PRIMES_10_BITS
    dp[0] = 1

    for i, cnt in counts.items():
        # bits representing the primes that n is a product of
        mask = PRIMES_10_MASKS[i]
        if cnt and mask:
            # Iterate over the existing 1024 prime_masks.
            for j in range(PRIMES_10_BITS):
                # In case new primes can be added to the mask.
                if j & mask == 0:
                    # The new count of subsets will be
                    # `dp[j]` * the count of the number in `a`
                    dp[j | mask] += dp[j] * cnt % m
    # Return the sum of counts for all possible sets of primes
    # minus empty set. Multiply by 2^(count of 1s).
    return ((sum(dp) - 1) * pow(2, counts[1], m)) % m
