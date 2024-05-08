"""Test module for NP-complete problems and puzzles."""

import unittest

import np_complete as npc


class TestNPComplete(unittest.TestCase):
    """Test class for the NP-complete problems and puzzle solutions."""

    def test_min_diff_set_partition(self):
        """Test `min_diff_set_partition`."""
        assert npc.min_diff_set_partition([1, 1]) == (1, 1)
        assert npc.min_diff_set_partition([-32, 9, 18]) == (-14, 9)
        assert npc.min_diff_set_partition([3, -3, 5, -2]) == (1, 2)
        assert npc.min_diff_set_partition([13, -17, 6, 48, -44, -14]) == (-10, 2)
        assert npc.min_diff_set_partition([6, 13, -17, 6, 48, -44, -14]) == (-2, 0)
        assert npc.min_diff_set_partition([3, 4, 5, -3, 100, 1, 89, 54, 23, 20]) == (
            148,
            148,
        )

    def test_just_add_operators(self):
        """Test `just_add_operators`."""
        assert npc.just_add_operators("2", 2) == ["2"]
        assert npc.just_add_operators("232", 8) == ["2+3*2", "2*3+2"]
        assert npc.just_add_operators("123", 6) == ["1+2+3", "1*2*3"]
        assert not npc.just_add_operators("3216", 19)
        assert npc.just_add_operators("1054", 4) == ["1*0*5+4"]
        assert not npc.just_add_operators("33", 14)
