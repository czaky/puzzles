"""Test module for the combinatorics related puzzles."""

import unittest

import combinatorics as c


class TestMatrixPuzzles(unittest.TestCase):
    """Test class for the matrix related puzzles."""

    def test_fib(self):
        "Test `fib."
        self.assertEqual(1, c.fib(0, 5))
        self.assertEqual(1, c.fib(2, 5))
        self.assertEqual(1, c.fib(1, 5))
        self.assertEqual(2, c.fib(3, 5))
        self.assertEqual(3, c.fib(4, 5))
        self.assertEqual(0, c.fib(5, 5))
        self.assertEqual(3, c.fib(6, 5))
        self.assertEqual(687995182, c.fib(100))

    def test_generic_fib(self):
        "Test `generic_fib."
        self.assertEqual(4, c.generic_fib(3, 3, 3, 3, 5))
