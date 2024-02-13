import unittest
from arrays import *

class TestRotatedArray(unittest.TestCase):

    def test_rotated_minimum(self):
        self.assertEqual(1, rotated_minimum([1, 2, 3, 4]))
        self.assertEqual(1, rotated_minimum([5, 1, 2, 3, 4]))
        self.assertEqual(1, rotated_minimum([2, 3, 4, 5, 1]))

class TestUnsortedArray(unittest.TestCase):

    def test_equilibrium_point(self):
        self.assertEqual(2, equilibrium_point([1, 3, 5, 2, 2]))
        self.assertEqual(1, equilibrium_point([8, 2, 3, 1, 4]))
        self.assertEqual(2, equilibrium_point([1, 2, 3, 3]))
        self.assertEqual(-1, equilibrium_point([1, 2, 3]))

    def test_duplicates(self):
        self.assertEqual([2], duplicates([1, 3, 5, 2, 2]))
        self.assertEqual([1, 2, 3], duplicates([2, 3, 2, 1, 2, 1, 3]))
        self.assertEqual([], duplicates([1, 2, 3]))

    def test_pairs_count(self):
        self.assertEqual(2, pairs_count([1, 3, 5, 2, 2], 7))
        self.assertEqual(7, pairs_count([2, 3, 2, 1, 2, 1, 3], 4))
        self.assertEqual(0, pairs_count([1, 2, 3], 6))

    def test_subrev(self):
        a = [1, 2, 3, 4, 5]
        subrev(a)
        self.assertEqual([5, 4, 3, 2, 1], a)

        a = [1, 2, 3, 4, 5]
        subrev(a, 1, 3)
        self.assertEqual([1, 4, 3, 2, 5], a)

        a = [1, 2, 3, 4, 5]
        subrev(a, -4, -2)
        self.assertEqual([1, 4, 3, 2, 5], a)

        a = [1, 2, 3, 4, 5]
        subrev(a, 0, 0)
        self.assertEqual([1, 2, 3, 4, 5], a)

        a = [1, 2, 3, 4, 5]
        subrev(a, 4, 4)
        self.assertEqual([1, 2, 3, 4, 5], a)

        a = [1, 2, 3, 4, 5]
        subrev(a, 0, 4)
        self.assertEqual([5, 4, 3, 2, 1], a)

    def test_rotate(self):
        a = [1, 2, 3, 4, 5]
        rotate(a)
        self.assertEqual([2, 3, 4, 5, 1], a)

        a = [1, 2, 3, 4, 5]
        rotate(a, 0)
        self.assertEqual([1, 2, 3, 4, 5], a)

        a = [1, 2, 3, 4, 5]
        rotate(a, 3)
        self.assertEqual([4, 5, 1, 2, 3], a)

        a = [1, 2, 3, 4, 5]
        rotate(a, 8)
        self.assertEqual([4, 5, 1, 2, 3], a)

        a = [1, 2, 3, 4, 5]
        rotate(a, -3)
        self.assertEqual([3, 4, 5, 1, 2], a)

    