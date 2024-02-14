"""Test module for the schedule or interval based puzzles."""

from typing import List
from functools import reduce

def meetings(start: List[int], end: List[int]) -> int:
    """
Returns maximum number of meetings that can be scheduled
in one room based on the meetings' `start` and `end` times.
"""
    return reduce(
        (lambda v, m: (v[0]+1, m[0]) if v[1] < m[1] else v),
        sorted(zip(end, start)), (0, -1))[0]
