"""Test module for the combinatorics related puzzles."""

import unittest

import combinatorics as c


class TestMatrixPuzzles(unittest.TestCase):
    """Test class for the matrix related puzzles."""

    def test_fib(self):
        """Test `fib."""
        assert c.fib(0, 5) == 1
        assert c.fib(2, 5) == 1
        assert c.fib(1, 5) == 1
        assert c.fib(3, 5) == 2
        assert c.fib(4, 5) == 3
        assert c.fib(5, 5) == 0
        assert c.fib(6, 5) == 3
        assert c.fib(100) == 687995182

    def test_generic_fib(self):
        """Test `generic_fib."""
        assert c.generic_fib(3, 3, 3, 3, 5) == 4

    def test_sum_of_456_numbers(self):
        assert c.sum_of_456_numbers(1, 0, 0) == 4
        assert c.sum_of_456_numbers(0, 1, 0) == 5
        assert c.sum_of_456_numbers(0, 0, 1) == 6
        assert c.sum_of_456_numbers(1, 1, 0) == 108
        assert c.sum_of_456_numbers(1, 0, 1) == 120
        assert c.sum_of_456_numbers(0, 1, 1) == 132
        assert c.sum_of_456_numbers(1, 1, 1) == 3675
        assert c.sum_of_456_numbers(3, 2, 1) == 34431574
        assert c.sum_of_456_numbers(1, 2, 3) == 39345806
