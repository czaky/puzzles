"""Binary Index Tree - used to calculate and update cumulative values in log(N)."""

import operator as op
from itertools import accumulate, islice, repeat
from typing import Callable, Iterable, List


class BinIndexTree:
    "Binary Index Tree."

    # This is a 0-indexed implementation.

    def __init__(self, arg: Iterable | int, operator: Callable = op.add):
        """Initialize the binary index tree.

        Args:
            arg (Iterable | int): an iterable with values or size of the tree.
            operator (Callable, optional): Cumulative operator. Defaults to `+`.
        """
        self.op = operator
        if isinstance(arg, Iterable):
            # log(N) construction - in-place.
            self.array = list(accumulate(arg, self.op))
            for i in reversed(range(1, len(self.array))):
                li = (i & (i + 1)) - 1  # lsb(i+1) -1
                if li >= 0:
                    self.array[i] -= self.array[li]
        elif isinstance(arg, int):
            self.array = [0.0] * arg
        else:
            assert isinstance(arg, Iterable | int)

    def add(self, i: int, value):
        "Add `value` to the tree at index `i`"
        while i < len(self.array):
            self.array[i] = self.op(self.array[i], value)
            i |= i + 1

    def sum(self, i: int):
        "Return cumulative sum at index `i`."
        s = 0
        while i >= 0:
            s = self.op(s, self.array[i])
            i = (i & (i + 1)) - 1  # lsb(i+1) -1
        return s


def maximum_broken_toys_queries(toys: List[int], queries: List[List[int]]) -> List[int]:
    """
    For each query return the maximum number of toys you can buy.
    The queries contain broken toy indices in addition to the cost-target.

    Parameters
    ----------
    toys : List[int]
        List of toy prices.
    queries : List[List[int]]
        Each query consist of [<cost-target>, <broken-count>, ... <broken-index>]

    Returns
    -------
    List[int]
        Sums of the non-broken toys that can fit the cost-target.
    """
    # O((N+Q*K)*logN + Q*logN*logN)
    # The idea is to use a binary index tree (BIT) to reduce the operation cost
    # of summing and updating to O(logN).
    # Another BIT is used to mark the broken trees.
    # Given that the toys array is unsorted,
    # we also have to derive a reverse sort index.
    n = len(toys)
    # Sort toys and derive the reverse sorting index (rix).
    rix = [0] * n
    for i, ri in enumerate(sorted(range(n), key=lambda i: toys[i])):
        rix[ri] = i
    toys.sort()
    bit = BinIndexTree(toys)
    # BIT of ones - to determine counts of unbroken stuff.
    ones = BinIndexTree(repeat(1, n))
    ans = []
    for q in queries:
        cost = q[0]
        # Translate the broken indexes to the sorted index.
        sbroken = list(rix[i - 1] for i in islice(q, 2, None))
        # Knock out broken toys.
        for i in sbroken:
            bit.add(i, -toys[i])
            ones.add(i, -1)
        # Binary search between 0 and n-1.
        tc, l, h = -1, 0, n - 1
        while l <= h:
            m = (l + h) // 2
            if bit.sum(m) <= cost:
                # Get the largest toys position at below or equal cost.
                tc = m
                l = m + 1
            else:
                h = m - 1
        ans.append(ones.sum(tc))
        # restore
        for i in sbroken:
            bit.add(i, toys[i])
            ones.add(i, 1)
    return ans
