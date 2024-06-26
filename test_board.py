"""Test module for the board puzzles."""

import unittest

import board as b


class TestBoardGames(unittest.TestCase):
    """Test class for the board games puzzles."""

    def test_queens(self):
        """Test the `queens` puzzle."""
        assert not b.queens(0)
        assert b.queens(1) == [[1]]
        assert not b.queens(2)
        assert not b.queens(3)
        assert b.queens(4) == [[2, 4, 1, 3], [3, 1, 4, 2]]
        assert b.queens(5) == [
            [1, 3, 5, 2, 4],
            [1, 4, 2, 5, 3],
            [2, 4, 1, 3, 5],
            [2, 5, 3, 1, 4],
            [3, 1, 4, 2, 5],
            [3, 5, 2, 4, 1],
            [4, 1, 3, 5, 2],
            [4, 2, 5, 3, 1],
            [5, 2, 4, 1, 3],
            [5, 3, 1, 4, 2],
        ]
