"""Test module for the matrix related puzzles."""

import unittest
import matrix as m

class TestMatrixPuzzles(unittest.TestCase):
    """Test class for the matrix related puzzles."""
    def test_find_sorted(self):
        "Test `find_sorted` function."
        self.assertTrue(m.find_sorted(
            [[3, 30, 38],
            [44, 52, 54],
            [57, 60, 69]], 52))
        self.assertTrue(m.find_sorted(
            [[3, 30, 38],
            [44, 52, 54],
            [57, 60, 69]], 38))
        self.assertTrue(m.find_sorted(
            [[3, 30, 38],
            [44, 52, 54],
            [57, 60, 69]], 57))
        self.assertTrue(m.find_sorted(
            [[3, 30, 38],
            [44, 52, 54],
            [57, 60, 69]], 69))
        self.assertTrue(m.find_sorted(
            [[3, 30, 38],
            [44, 52, 54],
            [57, 60, 69]], 3))
        self.assertFalse(m.find_sorted(
            [[3, 30, 38],
            [44, 52, 54],
            [57, 60, 69]], 62))
