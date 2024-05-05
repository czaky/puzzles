"""Test module for the board puzzles."""

import unittest

import board as b


class TestBoardGames(unittest.TestCase):
    """Test class for the board games puzzles."""

    def test_queens(self):
        """Test the `queens` puzzle."""
        assert b.queens(0) is []
        assert b.queens(1) == [[1]]
        assert b.queens(2) is []
        assert b.queens(3) is []
        assert b.queens(4) == [[3, 1, 4, 2], [2, 4, 1, 3]]
