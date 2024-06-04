"""Test module for the search."""

import unittest
from itertools import accumulate

import search as s
from strings import splint


class TestSearch(unittest.TestCase):
    """Test class for the search puzzles."""

    def test_largest_sum_cycle(self):
        """Test `largest_sum_cycle`."""
        assert s.largest_sum_cycle([2, 2, 1, 2, 2]) == 3
        assert s.largest_sum_cycle([1, 2, 0, -1]) == 3
        assert s.largest_sum_cycle([1, 2, 1]) == 3
        assert s.largest_sum_cycle([2, 0, -1, 2]) == -1
        e = [7, 3, -1, 1, 9, 0, 3, 5, 5, 3]
        assert s.largest_sum_cycle(e) == 12

    def test_geek_cake_distribution(self):
        """Test `geek_cake_distribution`."""
        assert s.geek_cake_distribution([1, 2, 3], 3) == 1
        assert s.geek_cake_distribution([6, 3, 2, 8, 7, 5], 3) == 9
        assert s.geek_cake_distribution([5, 6, 7, 8, 9, 1, 2, 3, 4], 9) == 1
        assert s.geek_cake_distribution([1, 2, 3, 4, 5, 6, 7, 8, 9], 6) == 6
        assert s.geek_cake_distribution([1, 2, 4, 7, 3, 6, 9], 4) == 7
        chunks = splint(
            """4 81 19 22 42 82 48 33 33 93 94 34 87 38 89 21 66 31 14 66 96 34 97 53
            33 36 76 70 75 74 4 58 44 49 21 48 46 39 33 95 68 44 23 56 46 94 70 92 79
            41 97 38 65 68 87 20 44 19 5 75 20 55 75 30 50 56 68 1 64 53 61 19 47 12 50
            82 77 40 29 27 36 12 34 76 46""",
        )
        assert s.geek_cake_distribution(chunks, 27) == 125

    def test_rotated_minimum(self):
        """Test `rotated_minimum` function."""
        assert s.rotated_minimum([1, 2, 3, 4]) == 1
        assert s.rotated_minimum([5, 1, 2, 3, 4]) == 1
        assert s.rotated_minimum([2, 3, 4, 5, 1]) == 1

    def test_equilibrium_point(self):
        """Test `equilibrium_point` function."""
        assert s.equilibrium_point([1, 3, 5, 2, 2]) == 2
        assert s.equilibrium_point([8, 2, 3, 1, 4]) == 1
        assert s.equilibrium_point([1, 2, 3, 3]) == 2
        assert s.equilibrium_point([1, 2, 3]) == -1

    def test_bitonic_point(self):
        """Test `bitonic_point` function."""
        assert s.bitonic_point([1, 3, 5]) == 5
        assert s.bitonic_point([1, 3, 5, 4]) == 5
        assert s.bitonic_point([1]) == 1

    def test_transition_point(self):
        """Test `transition_point`."""
        assert s.transition_point([1, 1, 1, 1]) == -1
        assert s.transition_point([0, 1, 1, 1]) == 0
        assert s.transition_point([0, 0, 1, 1]) == 1
        assert s.transition_point([0, 0, 0, 1]) == 2
        assert s.transition_point([0, 0, 0, 0]) == 3

    def test_find_extra_element(self):
        """Test `find_extra_element` function."""
        assert s.find_extra_element([1], []) == 0
        assert s.find_extra_element([1, 2], [1]) == 1
        assert s.find_extra_element([1, 2], [2]) == 0
        assert s.find_extra_element([1], [1, 2]) == 1
        assert s.find_extra_element([2], [1, 2]) == 0
        assert s.find_extra_element([1, 2, 3], [1, 2]) == 2
        assert s.find_extra_element([1, 2, 3], [2, 3]) == 0
        assert s.find_extra_element([1, 2, 3, 4, 5], [1, 2, 4, 5]) == 2

    def test_duplicated_sorted_find_unique(self):
        """Test `duplicated_sorted_find_unique` function."""
        assert s.duplicated_sorted_find_unique([1, 1, 5, 8, 8]) == 5
        assert s.duplicated_sorted_find_unique([1, 3, 3, 4, 4, 5, 5]) == 1
        assert s.duplicated_sorted_find_unique([1, 1, 3]) == 3

    def test_first_last(self):
        """Test `first_last` function."""
        assert s.first_last([1, 2, 3, 3, 3, 4], 1) == (0, 0)
        assert s.first_last([1, 2, 3, 3, 3, 4], 3) == (2, 4)
        assert s.first_last([1, 1, 2, 3, 3, 3, 4], 1) == (0, 1)
        assert s.first_last([1, 1, 2, 3, 3, 3, 4], 4) == (6, 6)
        assert s.first_last([1, 1, 2, 3, 4, 4, 4], 4) == (4, 6)
        assert s.first_last([1, 1, 2, 3, 4, 4, 4], 5) == (-1, -1)

    def test_partition_by_sum(self):
        """Test `partition_by_sum`."""
        cs = lambda a: list(accumulate(a, initial=0))
        assert s.partition_by_sum(cs([])) == (0, 0)
        assert s.partition_by_sum(cs([2])) == (0, 2)
        assert s.partition_by_sum(cs([2, 2])) == (2, 2)
        assert s.partition_by_sum(cs([2, 2, 2])) == (2, 4)
        assert s.partition_by_sum(cs([2, 2, 2, 2])) == (4, 4)

    def test_four_partitions_min_sum_difference(self):
        """Test `four_partitions_min_sum_difference`."""
        assert s.four_partitions_min_sum_difference([1, 2, 3, 4]) == 3
        assert s.four_partitions_min_sum_difference([1, 2, 3, 3, 4]) == 1
        ar = [16, 8, 11, 2, 12, 4, 11, 16, 15, 2, 5, 18, 7, 17]
        assert s.four_partitions_min_sum_difference(ar) == 13

    def test_water_distribution(self):
        assert s.water_distribution(
            [6, 4, 14, 17, 3, 15, 16, 5, 7, 11, 12],
            [5, 7, 16, 12, 2, 13, 6, 17, 1, 4, 8],
            [2, 2, 2, 4, 8, 2, 8, 8, 9, 9, 2],
        ) == [(3, 2, 8), (11, 1, 2), (14, 8, 2), (15, 13, 2)]
        assert s.water_distribution(
            [7, 5, 4, 2, 9, 3], [4, 9, 6, 8, 7, 1], [98, 72, 10, 22, 17, 66]
        ) == [(2, 8, 22), (3, 1, 66), (5, 6, 10)]
