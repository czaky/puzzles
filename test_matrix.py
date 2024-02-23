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


    def test_optimum_multiplications(self):
        "Test `optimum_multiplications`."
        self.assertEqual(580, m.optimum_multiplications([2, 40, 2, 40, 5]))
        self.assertEqual(26000, m.optimum_multiplications([40, 20, 30, 10, 30]))
