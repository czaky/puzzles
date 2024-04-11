"Bit manipulation related puzzles."

from math import log
from typing import List, Tuple


def count_different_bit_pairs(a: List[int]) -> int:
    """Count all bit differences for number pairs from array `a`.

    For each pair of integers in the array `a` sum all the differences in bits.
    """
    # The idea is to find the number of zero bit at each position for all the numbers.
    # This gives both the number of zero bits `z` and number of set bits `n-z`.
    # When multiplying `z * (n-z)`, get the number of bit differences at this position.
    # We sum this number of differences for all positions to get the overall diff count.
    #
    # Runs in O(N * log(max(n))).
    # Determine the length of the array and the bit length of maximum number.
    n, l = len(a), int(log(max(a), 2)) + 1
    # Compute the count of zero bits at each bit position.
    zeros = (sum(not x & b for x in a) for b in (1 << i for i in range(l)))
    # Sum the product of zero bits and set bits for each position.
    return sum((n - z) * z for z in zeros) * 2


class BitTrie:
    """A trie sorting integers with nodes splitting for each bit.

    Each node in the trie is just an array of two, with one cell for 0 and the other for 1.
    The leaf nodes are at the same distance of max `bits`.
    The leaf nodes also store the actual number as data.
    """

    def __init__(self, bits: int = 32):
        """Initialize the `BitTrie`.

        Args:
            bits (int, optional): Maximum number of bits for integers stored. Defaults to 32.
        """
        self.root = [0, 0]
        self.bits = bits

    def insert(self, num: int, data=0):
        "Insert `num` into the trie. Extra `data` can be stored with it."
        n: list = self.root
        for i in reversed(range(self.bits)):
            r = (num >> i) & 1
            n[r] = n[r] or [0, 0]
            n = n[r]
        # Store the `num` in the last node.
        n[:] = [num, data]

    def nearest(self, num: int):
        "Find the nearest number to `num`. Returns the number plus additional data."
        n: list = self.root
        for i in reversed(range(self.bits)):
            r = (num >> i) & 1
            # First lookup a similar bit,
            # otherwise lookup the opposite bit
            n = n[r] or n[1 - r]
        # The numeric value and data are stored in the last node.
        return n


def max_xor_sub_array(a: list) -> Tuple[int, list]:
    "For an array `a` of integers, find the largest XOR value of a sub-array."
    # The idea is to generate a cumulative XOR value,
    # and find the previous cumulative value which would result in the highest
    # XOR if applied to the current XOR value.
    #
    # Finding the previous XOR value can be done by maintaining a trie
    # with values stored so far. The lookup is done using the negative
    # current running xor value as this would give us the largest
    # result (i.e. ~v ^ v is the largest possible result.)
    # In the trie we look for the nearest value stored so far, descending
    # the tree by taking path matching the bits in the `~v` if possible.
    #
    # Build a bit trie using the longest bit_length.
    trie = BitTrie(bits=max(map(int.bit_length, a), default=1))
    # Insert 0 as the starter for the cumulative xor value.
    trie.insert(0, -1)
    mx = (0, 0, 0)  # (max-value, sub-start, sub-end-exclusive)
    cx = 0  # cumulative xor value for the array
    for i, e in enumerate(a):
        cx ^= e
        # First insert the new value.
        trie.insert(cx, i)
        # Then lookup the nearest `~cx` value in the trie.
        # By xoring cx and the the nearest negative,
        # we get the maximum result for this array prefix.
        # We can update the maximum result `mx` for the overall array.
        nearest = trie.nearest(~cx)
        mx = max(mx, (cx ^ nearest[0], nearest[1] + 1, i + 1))
    return mx[0], a[mx[1] : mx[2]]
