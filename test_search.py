"""Test module for the search."""

import unittest

import search as s


class TestSearch(unittest.TestCase):
    """Test class for the search puzzles."""

    def test_largest_sum_cycle(self):
        "Test `largest_sum_cycle`."
        self.assertEqual(3, s.largest_sum_cycle([2, 2, 1, 2, 2]))
        self.assertEqual(3, s.largest_sum_cycle([1, 2, 0, -1]))
        self.assertEqual(3, s.largest_sum_cycle([1, 2, 1]))
        self.assertEqual(-1, s.largest_sum_cycle([2, 0, -1, 2]))
        e = [7, 3, -1, 1, 9, 0, 3, 5, 5, 3]
        self.assertEqual(12, s.largest_sum_cycle(e))
