"""NP-complete problems and puzzles."""

from typing import List, Tuple


def min_diff_set_partition(a: List[int]) -> Tuple[int, int]:
    """
    Partition the array `a` into two (almost) equal sets.

    Return the two sums of the sets with the smallest difference between.
    The subsets need to differ in size by at most one element.

    Parameters
    ----------
    a : List[int]
        An array of integers.

    Returns
    -------
    Tuple[int, int]
        The sums of the two subsets with the smallest difference between.
    """

    def f(i, j, x, y):
        if j == i:
            x += sum(a[:i])
        elif j:
            return f(i - 1, j - 1, x + a[i - 1], f(i - 1, j, x, y))
        return (x, y)[abs(x) > abs(y)]

    ln, s = len(a), sum(a)
    s1 = f(ln, (ln + 1) // 2, (1 - s) // 2, sum(map(abs, a))) + s // 2
    ss = (s1, s - s1)
    return min(ss), max(ss)
