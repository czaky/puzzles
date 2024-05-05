"""Test module for the numbers related puzzles."""

import unittest
from math import comb

import mathematics as m


class TestNumbers(unittest.TestCase):
    """Test class for the numbers puzzles."""

    def test_floor_sqrt(self):
        """Test the `floor_sqrt` function."""
        assert m.floor_sqrt(0) == 0
        assert m.floor_sqrt(1) == 1
        assert m.floor_sqrt(2) == 1
        assert m.floor_sqrt(3) == 1
        assert m.floor_sqrt(4) == 2
        assert m.floor_sqrt(5) == 2
        assert m.floor_sqrt(6) == 2

    def test_frog_hops(self):
        """Test the `frog_hops` function."""
        assert m.frog_hops(0) == 0
        assert m.frog_hops(1) == 1
        assert m.frog_hops(2) == 2
        assert m.frog_hops(3) == 4
        assert m.frog_hops(4) == 7
        assert m.frog_hops(5) == 13
        assert m.frog_hops(6) == 24

    def test_josephus(self):
        """Validated solution to `josephus` problem."""
        assert m.josephus(0, 10) == 0
        assert m.josephus(7, 2) == 6

    def test_factorial_trailing_zeros(self):
        """Validated solution to `factorial_trailing_zeros` problem."""
        assert m.factorial_trailing_zeros(3) == 0
        assert m.factorial_trailing_zeros(5) == 1
        assert m.factorial_trailing_zeros(25) == 6

    def test_paths_in_matrix(self):
        """Validated solution to `paths_in_matrix` problem."""
        assert m.paths_in_matrix(1, 1) == 1
        assert m.paths_in_matrix(3, 3) == 6
        assert m.paths_in_matrix(12, 12) == 705432

    def test_closest_palindrome_number(self):
        """Test `closest_palindrome_number`."""
        assert m.closest_palindrome_number(0) == 0
        assert m.closest_palindrome_number(10) == 9
        assert m.closest_palindrome_number(100) == 99
        assert m.closest_palindrome_number(101) == 101
        assert m.closest_palindrome_number(1000) == 999
        assert m.closest_palindrome_number(1001) == 1001
        assert m.closest_palindrome_number(60) == 55
        assert m.closest_palindrome_number(197) == 202
        assert m.closest_palindrome_number(195) == 191

    def test_next_happy_number(self):
        """Test `next_happy_number`."""
        assert m.next_happy_number(1) == 7
        assert m.next_happy_number(3) == 7
        assert m.next_happy_number(7) == 10
        assert m.next_happy_number(10) == 13
        assert m.next_happy_number(1000) == 1003

    def test_prime_numbers(self):
        """Test `prime_numbers` generator."""
        assert list(m.prime_numbers(0)) is []
        assert list(m.prime_numbers(1)) is []
        assert [2] == list(m.prime_numbers(2))
        assert [2, 3] == list(m.prime_numbers(3))
        assert [2, 3] == list(m.prime_numbers(4))
        assert [2, 3, 5] == list(m.prime_numbers(5))
        assert [2, 3, 5] == list(m.prime_numbers(6))
        assert [2, 3, 5, 7] == list(m.prime_numbers(7))
        assert [2, 3, 5, 7, 11, 13, 17, 19] == list(m.prime_numbers(22))
        assert [2, 3, 5, 7, 11, 13, 17, 19, 23] == list(m.prime_numbers(23))
        assert [2, 3, 5, 7, 11, 13, 17, 19, 23] == list(m.prime_numbers(24))
        assert [2, 3, 5, 7, 11, 13, 17, 19, 23] == list(m.prime_numbers(25))
        assert len(list(m.prime_numbers(100000))) == 9592

    def test_prime_sum(self):
        """Test `prime_sum`."""
        assert m.prime_sum(4) == (2, 2)
        assert m.prime_sum(5) == (2, 3)
        assert m.prime_sum(6) == (3, 3)
        assert m.prime_sum(7) == (2, 5)
        assert m.prime_sum(9) == (2, 7)
        assert m.prime_sum(5250) == (13, 5237)
        assert m.prime_sum(7426) == (173, 7253)
        assert m.prime_sum(34096) == (173, 33923)

    def test_best_numbers(self):
        """Test `best_numbers`."""
        assert m.best_numbers(2, 1, 2, 3, 5) == 2
        assert m.best_numbers(4, 6, 7, 5, 3) == 4
        assert m.best_numbers(10000, 1, 5, 2, 5) == 716192774

    def test_find_nth_k_bit_number(self):
        """Test `find_nth_k_bit_number`."""
        assert m.find_nth_k_bit_number(2, 3) == 1
        assert m.find_nth_k_bit_number(5, 1) == 8
        assert m.find_nth_k_bit_number(6, 2) == 5

    def test_combmod(self):
        """Test `combmod`."""
        assert comb(1, 1) == m.combmod(1, 1, 7)
        assert comb(6, 2) % 7 == m.combmod(6, 2, 7)
        assert comb(6, 2) == m.combmod(6, 2, 23)
        assert comb(11, 7) % 23 == m.combmod(11, 7, 23)
