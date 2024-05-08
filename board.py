"""Puzzles related to board games."""

from __future__ import annotations


def queens(n: int) -> list:
    """Return a list of queen combinations for an `NxN` board."""
    sols = []
    s = [0] * n

    def rec(r: int, invalid: int) -> None:
        place = 1 | 1 << (n + r) | 1 << (n * 4 - r)
        for s[r] in range(1, n + 1):
            if not invalid & place:
                if r == 0:
                    sols.append(s[:])
                else:
                    rec(r - 1, invalid | place)
            place <<= 1

    if n > 0:
        rec(n - 1, 0)
    return sorted(sols)
