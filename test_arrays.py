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