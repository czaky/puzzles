"""Test module for packing related puzzles."""

import unittest

from packing import walls_coloring


class TestPacking(unittest.TestCase):
    """Test class for the packing puzzles."""

    def test_walls_coloring(self):
        "Test `walls_coloring`."
        self.assertEqual(-1, walls_coloring([]))
        self.assertEqual(-1, walls_coloring([[]]))
        self.assertEqual(-1, walls_coloring([[1], [2]]))
        self.assertEqual(7, walls_coloring([[7]]))
        self.assertEqual(5, walls_coloring([[1, 5, 7], [5, 8, 4]]))
        self.assertEqual(
            8, walls_coloring([[1, 5, 7], [5, 8, 4], [3, 2, 9], [1, 2, 4]])
        )
