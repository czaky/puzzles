"""Test module for the array/list related puzzles."""

import unittest
import arrays as ar

class TestRotatedArray(unittest.TestCase):
    """Test class for sorted, rotated array puzzles."""
    def test_rotated_minimum(self):
        "Test `rotated_minimum` function."
        self.assertEqual(1, ar.rotated_minimum([1, 2, 3, 4]))
        self.assertEqual(1, ar.rotated_minimum([5, 1, 2, 3, 4]))
        self.assertEqual(1, ar.rotated_minimum([2, 3, 4, 5, 1]))

class TestUnsortedArray(unittest.TestCase):
    """Test class for unsorted array puzzles."""
    def test_equilibrium_point(self):
        "Test `equilibrium_point` function."
        self.assertEqual(2, ar.equilibrium_point([1, 3, 5, 2, 2]))
        self.assertEqual(1, ar.equilibrium_point([8, 2, 3, 1, 4]))
        self.assertEqual(2, ar.equilibrium_point([1, 2, 3, 3]))
        self.assertEqual(-1, ar.equilibrium_point([1, 2, 3]))

    def test_duplicates(self):
        "Test `duplicates` function."
        self.assertEqual([2], ar.duplicates([1, 3, 5, 2, 2]))
        self.assertEqual([1, 2, 3], ar.duplicates([2, 3, 2, 1, 2, 1, 3]))
        self.assertEqual([], ar.duplicates([1, 2, 3]))

    def test_pairs_count(self):
        "Test `pairs_count` function."
        self.assertEqual(2, ar.pairs_count([1, 3, 5, 2, 2], 7))
        self.assertEqual(7, ar.pairs_count([2, 3, 2, 1, 2, 1, 3], 4))
        self.assertEqual(0, ar.pairs_count([1, 2, 3], 6))

    def test_subrev(self):
        "Test `subrev`, sub array reversal function."
        a = [1, 2, 3, 4, 5]
        ar.subrev(a)
        self.assertEqual([5, 4, 3, 2, 1], a)

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 1, 3)
        self.assertEqual([1, 4, 3, 2, 5], a)

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, -4, -2)
        self.assertEqual([1, 4, 3, 2, 5], a)

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 0, 0)
        self.assertEqual([1, 2, 3, 4, 5], a)

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 4, 4)
        self.assertEqual([1, 2, 3, 4, 5], a)

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 0, 4)
        self.assertEqual([5, 4, 3, 2, 1], a)

    def test_rotate(self):
        "Test `rotate` function."
        a = [1, 2, 3, 4, 5]
        ar.rotate(a)
        self.assertEqual([2, 3, 4, 5, 1], a)

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, 0)
        self.assertEqual([1, 2, 3, 4, 5], a)

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, 3)
        self.assertEqual([4, 5, 1, 2, 3], a)

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, 8)
        self.assertEqual([4, 5, 1, 2, 3], a)

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, -3)
        self.assertEqual([3, 4, 5, 1, 2], a)

    def test_transition_point(self):
        "Test `transition_point`."
        self.assertEqual(-1, ar.transition_point([1, 1, 1, 1]))
        self.assertEqual(0, ar.transition_point([0, 1, 1, 1]))
        self.assertEqual(1, ar.transition_point([0, 0, 1, 1]))
        self.assertEqual(2, ar.transition_point([0, 0, 0, 1]))
        self.assertEqual(3, ar.transition_point([0, 0, 0, 0]))

    def test_min_distance(self):
        "Test `min_distance` function."
        self.assertEqual(-1, ar.min_distance([1, 2, 3], 2, 4))
        self.assertEqual(1, ar.min_distance([1, 2, 3], 2, 3))
        self.assertEqual(1, ar.min_distance([1, 2, 3], 2, 1))
        self.assertEqual(2, ar.min_distance([1, 2, 3], 1, 3))

    def test_first_repeating_index(self):
        "Test `first_repeating_index` function."
        self.assertEqual(-1, ar.first_repeating_index([1, 2, 3]))
        self.assertEqual(0, ar.first_repeating_index([1, 1, 2, 3]))
        self.assertEqual(1, ar.first_repeating_index([1, 2, 3, 2]))
        self.assertEqual(2, ar.first_repeating_index([1, 2, 3, 3]))

    def test_dedup_sorted(self):
        "Test `dedup_sorted` function."
        a = [1, 2, 3]
        self.assertEqual(3, ar.dedup_sorted(a))
        self.assertEqual([1, 2, 3], a)
        a = [1, 3, 3, 4]
        self.assertEqual(3, ar.dedup_sorted(a))
        self.assertEqual([1, 3, 4, 4], a)
        a = [2, 2, 2, 3]
        self.assertEqual(2, ar.dedup_sorted(a))
        self.assertEqual([2, 3, 2, 3], a)
