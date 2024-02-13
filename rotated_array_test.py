import unittest
from rotated_array import *

class TestRotatedArray(unittest.TestCase):
    def test_find_minimum(self):
        self.assertEqual(1, find_minimum([1, 2, 3, 4]))
        self.assertEqual(1, find_minimum([5, 1, 2, 3, 4]))
        self.assertEqual(1, find_minimum([2, 3, 4, 5, 1]))