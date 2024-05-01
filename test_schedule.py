"""Test module for the schedule or interval based puzzles."""

import unittest

import schedule as s


class TestSchedule(unittest.TestCase):
    """Test class for the schedule or interval based puzzles."""

    def test_meetings(self):
        "Test `meetings` function."
        self.assertEqual(1, s.meetings([1], [2]))
        self.assertEqual(4, s.meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
        self.assertEqual(1, s.meetings([1], [2]))
