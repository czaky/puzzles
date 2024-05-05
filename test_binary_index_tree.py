"""Tests for Binary Index Tree and related problems."""

import unittest

import binary_index_tree as bit
from binary_index_tree import BinIndexTree


class TestBinIndexTree(unittest.TestCase):
    """Test class for the binary index tree code."""

    def test_init(self):
        """Test bit `__init__`."""
        b = BinIndexTree([1, 2, 3])
        assert b.sum(0) == 1
        assert b.sum(1) == 3
        assert b.sum(2) == 6

        b = BinIndexTree([3, 2, 1])
        assert b.sum(0) == 3
        assert b.sum(1) == 5
        assert b.sum(2) == 6

    def test_add(self):
        """Test `add` function."""
        b = BinIndexTree([3, 2, 1])
        b.add(1, 5)
        assert b.sum(0) == 3
        assert b.sum(1) == 10
        assert b.sum(2) == 11
        b.add(0, -5)
        assert b.sum(0) == -2
        assert b.sum(1) == 5
        assert b.sum(2) == 6
        b.add(2, -5)
        assert b.sum(0) == -2
        assert b.sum(1) == 5
        assert b.sum(2) == 1


class TestBITPuzzles(unittest.TestCase):
    """Test class for the binary index tree puzzles."""

    def test_maximum_broken_toys_queries(self):
        """Test bit `maximum_broken_toys_queries`."""
        toys = [10, 8, 10, 5, 5, 7, 7, 10, 10, 6]
        queries = [
            [4, 6, 1, 9, 3, 7, 2, 8],
            [8, 4, 2, 4, 1, 7],
            [6, 7, 10, 6, 4, 9, 5, 7, 1],
            [9, 5, 4, 5, 6, 2, 1],
            [1, 9, 10, 1, 9, 5, 4, 3, 8, 7, 2],
            [9, 4, 7, 10, 6, 9],
        ]
        assert [0, 1, 0, 1, 0, 1] == bit.maximum_broken_toys_queries(toys, queries)
        toys = [9, 7, 2, 1, 9, 4, 2, 9, 5, 8]
        queries = [
            [1, 2, 6, 7],
            [9, 1, 10],
            [5, 6, 6, 7, 3, 8, 9, 10],
            [10, 5, 9, 1, 2, 3, 5],
            [3, 0],
            [4, 0],
            [2, 2, 10, 5],
            [9, 6, 4, 1, 2, 6, 3, 7],
            [10, 8, 9, 3, 6, 5, 1, 2, 8, 4],
            [10, 5, 5, 10, 4, 9, 1],
        ]
        assert [1, 4, 1, 3, 2, 2, 1, 1, 2, 3] == bit.maximum_broken_toys_queries(
            toys,
            queries,
        )
