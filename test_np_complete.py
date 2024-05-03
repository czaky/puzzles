"""Test module for NP-complete problems and puzzles."""

import unittest

import np_complete as npc


class TestNPComplete(unittest.TestCase):
    """Test class for the NP-complete problems and puzzle solutions."""

    def test_min_diff_set_partition(self):
        "Test `min_diff_set_partition`."
        self.assertEqual((1, 1), npc.min_diff_set_partition([1, 1]))
        self.assertEqual((-14, 9), npc.min_diff_set_partition([-32, 9, 18]))
        self.assertEqual((1, 2), npc.min_diff_set_partition([3, -3, 5, -2]))
        self.assertEqual(
            (-10, 2), npc.min_diff_set_partition([13, -17, 6, 48, -44, -14])
        )
        self.assertEqual(
            (-2, 0), npc.min_diff_set_partition([6, 13, -17, 6, 48, -44, -14])
        )
        self.assertEqual(
            (148, 148),
            npc.min_diff_set_partition([3, 4, 5, -3, 100, 1, 89, 54, 23, 20]),
        )
