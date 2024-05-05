"""Test module for the search."""

import unittest

import search as s
from strings import splint


class TestSearch(unittest.TestCase):
    """Test class for the search puzzles."""

    def test_largest_sum_cycle(self):
        """Test `largest_sum_cycle`."""
        assert s.largest_sum_cycle([2, 2, 1, 2, 2]) == 3
        assert s.largest_sum_cycle([1, 2, 0, -1]) == 3
        assert s.largest_sum_cycle([1, 2, 1]) == 3
        assert s.largest_sum_cycle([2, 0, -1, 2]) == -1
        e = [7, 3, -1, 1, 9, 0, 3, 5, 5, 3]
        assert s.largest_sum_cycle(e) == 12

    def test_geek_cake_distribution(self):
        """Test `geek_cake_distribution`."""
        assert s.geek_cake_distribution([1, 2, 3], 3) == 1
        assert s.geek_cake_distribution([6, 3, 2, 8, 7, 5], 3) == 9
        assert s.geek_cake_distribution([5, 6, 7, 8, 9, 1, 2, 3, 4], 9) == 1
        assert s.geek_cake_distribution([1, 2, 3, 4, 5, 6, 7, 8, 9], 6) == 6
        assert s.geek_cake_distribution([1, 2, 4, 7, 3, 6, 9], 4) == 7
        chunks = splint(
            """4 81 19 22 42 82 48 33 33 93 94 34 87 38 89 21 66 31 14 66 96 34 97 53
            33 36 76 70 75 74 4 58 44 49 21 48 46 39 33 95 68 44 23 56 46 94 70 92 79
            41 97 38 65 68 87 20 44 19 5 75 20 55 75 30 50 56 68 1 64 53 61 19 47 12 50
            82 77 40 29 27 36 12 34 76 46""",
        )
        assert s.geek_cake_distribution(chunks, 27) == 125
