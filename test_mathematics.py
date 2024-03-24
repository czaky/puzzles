"""Test module for the numbers related puzzles."""

import unittest
import mathematics as m


class TestNumbers(unittest.TestCase):
    """Test class for the numbers puzzles."""

    def test_floor_sqrt(self):
        "Test the `floor_sqrt` function."
        self.assertEqual(0, m.floor_sqrt(0))
        self.assertEqual(1, m.floor_sqrt(1))
        self.assertEqual(1, m.floor_sqrt(2))
        self.assertEqual(1, m.floor_sqrt(3))
        self.assertEqual(2, m.floor_sqrt(4))
        self.assertEqual(2, m.floor_sqrt(5))
        self.assertEqual(2, m.floor_sqrt(6))

    def test_frog_hops(self):
        "Test the `frog_hops` function."
        self.assertEqual(0, m.frog_hops(0))
        self.assertEqual(1, m.frog_hops(1))
        self.assertEqual(2, m.frog_hops(2))
        self.assertEqual(4, m.frog_hops(3))
        self.assertEqual(7, m.frog_hops(4))
        self.assertEqual(13, m.frog_hops(5))
        self.assertEqual(24, m.frog_hops(6))

    def test_josephus(self):
        "Validated solution to `josephus` problem."
        self.assertEqual(0, m.josephus(0, 10))
        self.assertEqual(6, m.josephus(7, 2))

    def test_factorial_trailing_zeros(self):
        "Validated solution to `factorial_trailing_zeros` problem."
        self.assertEqual(0, m.factorial_trailing_zeros(3))
        self.assertEqual(1, m.factorial_trailing_zeros(5))
        self.assertEqual(6, m.factorial_trailing_zeros(25))

    def test_paths_in_matrix(self):
        "Validated solution to `paths_in_matrix` problem."
        self.assertEqual(1, m.paths_in_matrix(1, 1))
        self.assertEqual(6, m.paths_in_matrix(3, 3))
        self.assertEqual(705432, m.paths_in_matrix(12, 12))

    def test_closest_palindrome_number(self):
        "Test `closest_palindrome_number`."
        self.assertEqual(0, m.closest_palindrome_number(0))
        self.assertEqual(9, m.closest_palindrome_number(10))
        self.assertEqual(99, m.closest_palindrome_number(100))
        self.assertEqual(101, m.closest_palindrome_number(101))
        self.assertEqual(999, m.closest_palindrome_number(1000))
        self.assertEqual(1001, m.closest_palindrome_number(1001))
        self.assertEqual(55, m.closest_palindrome_number(60))
        self.assertEqual(202, m.closest_palindrome_number(197))
        self.assertEqual(191, m.closest_palindrome_number(195))
