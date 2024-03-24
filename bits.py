"Bit manipulation related puzzles."

from math import log
from typing import List


def count_different_bit_pairs(a: List[int]) -> int:
    "Count all bit differences for number pairs from array `a`."
    # Runs in O(N * log(max(n))).
    # Determine the length of the array and the bit length of maximum number.
    n, l = len(a), int(log(max(a), 2)) + 1
    # Compute the count of zero bits at each bit position.
    zeros = (sum(not x & b for x in a) for b in (1 << i for i in range(l)))
    # Sum the product of zero bits and set bits for each position.
    return sum((n - z) * z for z in zeros) * 2
