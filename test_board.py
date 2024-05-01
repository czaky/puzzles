"""Test module for the board puzzles."""

import unittest

import board as b


class TestBoardGames(unittest.TestCase):
    """Test class for the board games puzzles."""

    def test_queens(self):
        "Test the `queens` puzzle."
        self.assertEqual([], b.queens(0))
        self.assertEqual([[1]], b.queens(1))
        self.assertEqual([], b.queens(2))
        self.assertEqual([], b.queens(3))
        self.assertEqual([[3, 1, 4, 2], [2, 4, 1, 3]], b.queens(4))
