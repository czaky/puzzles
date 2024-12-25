"""Test module for the sorting algorithms and related puzzles' solutions."""

from __future__ import annotations

import unittest

import sorting as s


class TestSorting(unittest.TestCase):
    """Test class for the sorting code and puzzles."""

    def _test(self, algorithm: callable) -> None:
        def sort(array: list) -> list:
            copy = array[:]
            algorithm(copy)
            return copy

        assert not sort([])
        assert sort([1]) == [1]
        assert sort([1, 2]) == [1, 2]
        assert sort([2, 1]) == [1, 2]
        assert sort([1, 1]) == [1, 1]

        assert sort([1, 2, 3]) == [1, 2, 3]
        assert sort([1, 3, 2]) == [1, 2, 3]
        assert sort([2, 1, 3]) == [1, 2, 3]
        assert sort([2, 3, 1]) == [1, 2, 3]
        assert sort([3, 1, 2]) == [1, 2, 3]
        assert sort([3, 2, 1]) == [1, 2, 3]

        assert sort([1, 2, 2]) == [1, 2, 2]
        assert sort([2, 1, 2]) == [1, 2, 2]
        assert sort([2, 2, 1]) == [1, 2, 2]

        assert sort([2, 3, 4, 5]) == [2, 3, 4, 5]
        assert sort([7, 6, 5, 4]) == [4, 5, 6, 7]
        assert sort([7, 7, 5, 3]) == [3, 5, 7, 7]
        assert sort([8, 3, 4, 3]) == [3, 3, 4, 8]
        assert sort([8, 3, 4, 4]) == [3, 4, 4, 8]

        assert sort([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
        assert sort([9, 8, 7, 6, 5, 4]) == [4, 5, 6, 7, 8, 9]
        assert sort([9, 8, 7, 7, 5, 3]) == [3, 5, 7, 7, 8, 9]
        assert sort([9, 4, 8, 4, 5, 3]) == [3, 4, 4, 5, 8, 9]
        assert sort([9, 4, 8, 3, 5, 4]) == [3, 4, 4, 5, 8, 9]

        assert sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert sort([9, 8, 7, 7, 5, 3, 3, 2, 1, 0]) == [0, 1, 2, 3, 3, 5, 7, 7, 8, 9]
        assert sort([9, 4, 8, 4, 5, 3, 3, 2, 1, 0]) == [0, 1, 2, 3, 3, 4, 4, 5, 8, 9]
        assert sort([9, 4, 8, 4, 5, 3, 3, 2, 4, 0]) == [0, 2, 3, 3, 4, 4, 4, 5, 8, 9]

    def test_selection_sort(self):
        self._test(s.selection)

    def test_bubble_sort(self):
        self._test(s.bubble)

    def test_insertion_sort(self):
        self._test(s.insertion)

    def test_gnome_sort(self):
        self._test(s.gnome)

    def test_quick_sort(self):
        self._test(s.quick)

    def test_quick_simple_sort(self):
        self._test(s.quick_simple)

    def test_merge_sort(self):
        self._test(s.merge)

    def test_merge_rec_sort(self):
        self._test(s.merge_rec)
