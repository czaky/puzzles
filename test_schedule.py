"""Test module for the schedule or interval based puzzles."""

import unittest

import schedule as s


class TestSchedule(unittest.TestCase):
    """Test class for the schedule or interval based puzzles."""

    def test_meetings(self):
        """Test `meetings` function."""
        assert s.meetings([1], [2]) == 1
        assert s.meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]) == 4
        assert s.meetings([1], [2]) == 1
