"""Test module for the graph based puzzles."""

import unittest

import etc


class TestEtc(unittest.TestCase):
    """Test class for testing puzzles."""

    def test_pickup_min_time(self):
        """Test `pickup_min_time`."""
        assert etc.fruit_pickup_min_time([1, 3, 5, 7], [1, 2, 3, 1]) == 18
        assert etc.fruit_pickup_min_time([-4, -3, 1, -8], [4, 2, 4, 5]) == 24
        assert (
            etc.fruit_pickup_min_time([1, -8, -1, 2, -2, -5], [3, 3, 3, 4, 2, 1]) == 26
        )
