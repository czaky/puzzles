"""Test module for the board puzzles."""

import unittest

import board as b


class TestBoardGames(unittest.TestCase):
    """Test class for the board games puzzles."""

    def test_queens(self):
        """Test the `queens` puzzle."""
        assert [] == b.queens(0)
        assert [[1]] == b.queens(1)
        assert [] == b.queens(2)
        assert [] == b.queens(3)
        assert [[3, 1, 4, 2], [2, 4, 1, 3]] == b.queens(4)
