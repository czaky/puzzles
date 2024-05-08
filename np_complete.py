"""NP-complete problems and puzzles."""

from __future__ import annotations


def min_diff_set_partition(a: list[int]) -> tuple[int, int]:
    """Partition the array `a` into two (almost) equal sets.

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

    def f(i: int, j: int, x: int, y: int) -> int:
        if j == i:
            x += sum(a[:i])
        elif j:
            return f(i - 1, j - 1, x + a[i - 1], f(i - 1, j, x, y))
        return (x, y)[abs(x) > abs(y)]

    ln, s = len(a), sum(a)
    s1 = f(ln, (ln + 1) // 2, (1 - s) // 2, sum(map(abs, a))) + s // 2
    ss = (s1, s - s1)
    return min(ss), max(ss)


def just_add_operators(s: str, target: int) -> list:
    """Return expression with value equal to `target` by adding +, -, * to `s`.

    The operators are inserted between digits of `s`.
    A literal cannot start with leading zero.

    Parameters
    ----------
    s : str
        string of digits
    target : int
        target value

    Returns
    -------
    list
        a list of expressions created from `s` by adding: +, -, * operators

    """
    n = len(s)
    ret = []

    def split(i: int, expr: str, v: int, prev: int) -> None:
        # i - index for the suffix.
        # expr - expression built so far
        # v - value of the expression
        # prev - previously added component, used to backtrack on multiplication.
        if i >= n:
            if v == target:
                ret.append(expr)
            return

        for j in range(i + 1, min(n, i + 1 if s[i] == "0" else n) + 1):
            ns = s[i:j]
            nv = int(ns)
            split(j, expr + "+" + ns, v + nv, nv)
            split(j, expr + "-" + ns, v - nv, -nv)
            # Remove `prev` from the sum and add `prev * nv`.
            split(j, expr + "*" + ns, v - prev + prev * nv, prev * nv)


    for i in range(1, n + 1):
        ns = s[:i]
        nv = int(ns)
        split(i, ns, nv, nv)

    return ret
