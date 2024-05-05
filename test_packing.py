"""Test module for packing related puzzles."""

import unittest

from packing import walls_coloring


class TestPacking(unittest.TestCase):
    """Test class for the packing puzzles."""

    def test_walls_coloring(self):
        """Test `walls_coloring`."""
        assert walls_coloring([]) == -1
        assert walls_coloring([[]]) == -1
        assert walls_coloring([[1], [2]]) == -1
        assert walls_coloring([[7]]) == 7
        assert walls_coloring([[1, 5, 7], [5, 8, 4]]) == 5
        assert walls_coloring([[1, 5, 7], [5, 8, 4], [3, 2, 9], [1, 2, 4]]) == 8
