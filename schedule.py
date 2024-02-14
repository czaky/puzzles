"""Test module for the schedule or interval based puzzles."""

from typing import List

def meetings(start: List[int], end: List[int]) -> int:
    """
Returns maximum number of meetings that can be scheduled
in one room based on the meetings' `start` and `end` times.
"""
    t = -1
    c = 0
    for e, s in sorted(zip(end, start)):
        if t < s:
            t = e
            c += 1
    return c
