"""Test module for the schedule or interval based puzzles."""

from __future__ import annotations

from functools import reduce


def meetings(start: list[int], end: list[int]) -> int:
    """Return maximum number of meetings that can be scheduled.

    The meetings are scheduled  in one room based on the meetings
    `start` and `end` times.
    """
    return reduce(
        (lambda v, m: (v[0] + 1, m[0]) if v[1] < m[1] else v),
        sorted(zip(end, start)),
        (0, -1),
    )[0]
