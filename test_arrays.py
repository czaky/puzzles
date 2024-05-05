"""Test module for the array/list related puzzles."""

import unittest

import arrays as ar


class TestRotatedArray(unittest.TestCase):
    """Test class for sorted, rotated array puzzles."""

    def test_rotated_minimum(self):
        """Test `rotated_minimum` function."""
        assert ar.rotated_minimum([1, 2, 3, 4]) == 1
        assert ar.rotated_minimum([5, 1, 2, 3, 4]) == 1
        assert ar.rotated_minimum([2, 3, 4, 5, 1]) == 1


class TestUnsortedArray(unittest.TestCase):
    """Test class for unsorted array puzzles."""

    def test_equilibrium_point(self):
        """Test `equilibrium_point` function."""
        assert ar.equilibrium_point([1, 3, 5, 2, 2]) == 2
        assert ar.equilibrium_point([8, 2, 3, 1, 4]) == 1
        assert ar.equilibrium_point([1, 2, 3, 3]) == 2
        assert ar.equilibrium_point([1, 2, 3]) == -1

    def test_bitonic_point(self):
        """Test `bitonic_point` function."""
        assert ar.bitonic_point([1, 3, 5]) == 5
        assert ar.bitonic_point([1, 3, 5, 4]) == 5
        assert ar.bitonic_point([1]) == 1

    def test_duplicates(self):
        """Test `duplicates` function."""
        assert [2] == ar.duplicates([1, 3, 5, 2, 2])
        assert [1, 2, 3] == ar.duplicates([2, 3, 2, 1, 2, 1, 3])
        assert [] == ar.duplicates([1, 2, 3])

    def test_pairs_count(self):
        """Test `pairs_count` function."""
        assert ar.pairs_count([1, 3, 5, 2, 2], 7) == 2
        assert ar.pairs_count([2, 3, 2, 1, 2, 1, 3], 4) == 7
        assert ar.pairs_count([1, 2, 3], 6) == 0

    def test_subrev(self):
        """Test `subrev`, sub array reversal function."""
        a = [1, 2, 3, 4, 5]
        ar.subrev(a)
        assert [5, 4, 3, 2, 1] == a

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 1, 3)
        assert [1, 4, 3, 2, 5] == a

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, -4, -2)
        assert [1, 4, 3, 2, 5] == a

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 0, 0)
        assert [1, 2, 3, 4, 5] == a

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 4, 4)
        assert [1, 2, 3, 4, 5] == a

        a = [1, 2, 3, 4, 5]
        ar.subrev(a, 0, 4)
        assert [5, 4, 3, 2, 1] == a

    def test_rotate(self):
        """Test `rotate` function."""
        a = [1, 2, 3, 4, 5]
        ar.rotate(a)
        assert [2, 3, 4, 5, 1] == a

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, 0)
        assert [1, 2, 3, 4, 5] == a

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, 3)
        assert [4, 5, 1, 2, 3] == a

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, 8)
        assert [4, 5, 1, 2, 3] == a

        a = [1, 2, 3, 4, 5]
        ar.rotate(a, -3)
        assert [3, 4, 5, 1, 2] == a

    def test_transition_point(self):
        """Test `transition_point`."""
        assert ar.transition_point([1, 1, 1, 1]) == -1
        assert ar.transition_point([0, 1, 1, 1]) == 0
        assert ar.transition_point([0, 0, 1, 1]) == 1
        assert ar.transition_point([0, 0, 0, 1]) == 2
        assert ar.transition_point([0, 0, 0, 0]) == 3

    def test_min_distance(self):
        """Test `min_distance` function."""
        assert ar.min_distance([1, 2, 3], 2, 4) == -1
        assert ar.min_distance([1, 2, 3], 2, 3) == 1
        assert ar.min_distance([1, 2, 3], 2, 1) == 1
        assert ar.min_distance([1, 2, 3], 1, 3) == 2

    def test_first_repeating_index(self):
        """Test `first_repeating_index` function."""
        assert ar.first_repeating_index([1, 2, 3]) == -1
        assert ar.first_repeating_index([1, 1, 2, 3]) == 0
        assert ar.first_repeating_index([1, 2, 3, 2]) == 1
        assert ar.first_repeating_index([1, 2, 3, 3]) == 2

    def test_dedup_sorted(self):
        """Test `dedup_sorted` function."""
        a = [1, 2, 3]
        assert ar.dedup_sorted(a) == 3
        assert [1, 2, 3] == a
        a = [1, 3, 3, 4]
        assert ar.dedup_sorted(a) == 3
        assert [1, 3, 4, 4] == a
        a = [2, 2, 2, 3]
        assert ar.dedup_sorted(a) == 2
        assert [2, 3, 2, 3] == a

    def test_meta_cafeteria(self):
        """Test `meta_cafeteria` puzzle."""
        assert ar.meta_cafeteria(10, 1, [2, 6]) == 3
        assert ar.meta_cafeteria(15, 2, [11, 6, 14]) == 1

    def test_product_except_self(self):
        """Test `product_except_self`."""
        assert [0, 0, 0, 1800, 0, 0] == ar.product_except_self([10, 3, 5, 0, 6, 2])
        assert [180, 600, 360, 300, 900] == ar.product_except_self([10, 3, 5, 6, 2])

    def test_count_triplets(self):
        """Test `count_triplets`."""
        assert ar.count_triplets([1, 5, 3, 2]) == 2
        assert ar.count_triplets([10, 3, 5, 6, 2]) == 1

    def test_greater_smaller(self):
        """Validate `greater_smaller` puzzle solution."""
        assert ar.greater_smaller([10, 6, 3, 1, 5, 11, 6, 1, 11, 12]) == 11
        assert ar.greater_smaller([10, 6, 3, 1, 5, 13, 6, 1, 11, 12]) is None
        assert ar.greater_smaller([10, 6, 3]) is None
        assert ar.greater_smaller([6, 3, 10]) is None

    def test_smallest_sub_with_greater_sum(self):
        """Test `smallest_sub_with_greater_sum` function."""
        assert ar.smallest_sub_with_greater_sum([255], 333) == 0
        assert ar.smallest_sub_with_greater_sum([255], 111) == 1
        assert ar.smallest_sub_with_greater_sum([1, 4, 45, 6, 0, 19], 51) == 3
        assert ar.smallest_sub_with_greater_sum([1, 4, 3, 6, 42, 4], 51) == 3
        assert ar.smallest_sub_with_greater_sum([45, 4, 3, 6, 2, 4], 51) == 3

    def test_window_distinct_count(self):
        """Test `window_distinct_count`."""
        assert [5, 5] == ar.window_distinct_count([10, 3, 5, 0, 6, 2], 5)
        assert [2, 2, 2, 2] == ar.window_distinct_count([10, 3, 5, 6, 2], 2)
        assert [3, 4, 4, 3] == ar.window_distinct_count([1, 2, 1, 3, 4, 2, 3], 4)

    def test_find_extra_element(self):
        """Test `find_extra_element` function."""
        assert ar.find_extra_element([1], []) == 0
        assert ar.find_extra_element([1, 2], [1]) == 1
        assert ar.find_extra_element([1, 2], [2]) == 0
        assert ar.find_extra_element([1], [1, 2]) == 1
        assert ar.find_extra_element([2], [1, 2]) == 0
        assert ar.find_extra_element([1, 2, 3], [1, 2]) == 2
        assert ar.find_extra_element([1, 2, 3], [2, 3]) == 0
        assert ar.find_extra_element([1, 2, 3, 4, 5], [1, 2, 4, 5]) == 2

    def test_pascal_triangle_row(self):
        """Test `test_pascal_triangle_row` function."""
        assert [1] == ar.pascal_triangle_row(1)
        assert [1, 1] == ar.pascal_triangle_row(2)
        assert [1, 2, 1] == ar.pascal_triangle_row(3)
        assert [1, 3, 3, 1] == ar.pascal_triangle_row(4)

    def test_min_diff(self):
        """Test `min_diff` function."""
        assert ar.min_diff([1, 9, 5, 11, 2], 3) == 4
        assert ar.min_diff([2, 30, 8, 11, 20, 1, 3], 4) == 7
        assert ar.min_diff([1, 7, 3], 2) == 2

    def test_duplicated_sorted_find_unique(self):
        """Test `duplicated_sorted_find_unique` function."""
        assert ar.duplicated_sorted_find_unique([1, 1, 5, 8, 8]) == 5
        assert ar.duplicated_sorted_find_unique([1, 3, 3, 4, 4, 5, 5]) == 1
        assert ar.duplicated_sorted_find_unique([1, 1, 3]) == 3

    def test_max_equal_zero_and_one_length(self):
        """Test `max_equal_zero_and_one_length` function."""
        assert ar.max_equal_zero_and_one_length([1, 0, 1, 0, 1]) == 4
        assert ar.max_equal_zero_and_one_length([1, 0, 1, 1, 1, 0, 0]) == 6
        assert ar.max_equal_zero_and_one_length([0, 0, 1]) == 2
        assert ar.max_equal_zero_and_one_length([0]) == 0
        assert ar.max_equal_zero_and_one_length([]) == 0

    def test_toys_with_budget(self):
        """Test `toys_with_budget` function."""
        assert ar.toys_with_budget([60, 5, 4, 3, 2, 20], 15) == 4
        assert ar.toys_with_budget([30, 20, 50], 100) == 3

    def test_first_last(self):
        """Test `first_last` function."""
        assert ar.first_last([1, 2, 3, 3, 3, 4], 1) == (0, 0)
        assert ar.first_last([1, 2, 3, 3, 3, 4], 3) == (2, 4)
        assert ar.first_last([1, 1, 2, 3, 3, 3, 4], 1) == (0, 1)
        assert ar.first_last([1, 1, 2, 3, 3, 3, 4], 4) == (6, 6)
        assert ar.first_last([1, 1, 2, 3, 4, 4, 4], 4) == (4, 6)
        assert ar.first_last([1, 1, 2, 3, 4, 4, 4], 5) == (-1, -1)

    def test_merge_sorted(self):
        """Test `merge_sorted` function."""
        a = [4, 5, 6, 12, 13]
        b = [0, 7, 8, 13, 12, 15]
        ar.merge_sorted(a, b)
        assert [0, 4, 5, 6, 7] == a
        assert [8, 12, 12, 13, 13, 15] == b
        a, b = b, a
        ar.merge_sorted(a, b)
        assert [0, 4, 5, 6, 7, 8] == a
        assert [12, 12, 13, 13, 15] == b

    def test_min_partition_diff(self):
        """Test `min_partition_diff` function."""
        assert ar.min_partition_diff([1]) == 1
        assert ar.min_partition_diff([1, 2]) == 1
        assert ar.min_partition_diff([2, 1]) == 1
        assert ar.min_partition_diff([5, 2]) == 3
        assert ar.min_partition_diff([2, 5]) == 3
        assert ar.min_partition_diff([60, 5, 4, 3, 2, 20]) == 26
        assert ar.min_partition_diff([30, 20, 50]) == 0

    def test_max_histogram_rectangle(self):
        """Test `max_histogram_rectangle` function."""
        assert ar.max_histogram_rectangle([6]) == 6
        assert ar.max_histogram_rectangle([3, 2]) == 4
        assert ar.max_histogram_rectangle([2, 3]) == 4
        assert ar.max_histogram_rectangle([3, 2, 1]) == 4
        assert ar.max_histogram_rectangle([2, 3, 1]) == 4
        assert ar.max_histogram_rectangle([1, 3, 2]) == 4
        assert ar.max_histogram_rectangle([1, 2, 3]) == 4
        assert ar.max_histogram_rectangle([6, 2, 5, 4, 5, 1, 6]) == 12
        assert ar.max_histogram_rectangle([1, 2, 1, 2, 1, 2, 1]) == 7

    def test_median2(self):
        """Test `median2` function."""
        assert ar.median2([1, 2, 3], [4, 6]) == 3
        assert ar.median2([1, 2, 3], [4, 5, 6]) == 3.5

    def test_next_smallest_palindrome(self):
        """Test `next_smallest_palindrome` function."""
        assert not ar.next_smallest_palindrome_number([])
        assert [1] == ar.next_smallest_palindrome_number([0])
        assert [8] == ar.next_smallest_palindrome_number([7])
        assert [1, 1] == ar.next_smallest_palindrome_number([9])
        assert [6, 6] == ar.next_smallest_palindrome_number([6, 1])
        assert [1, 0, 1] == ar.next_smallest_palindrome_number([9, 9])
        assert [2, 4, 4, 2] == ar.next_smallest_palindrome_number([2, 3, 4, 5])
        assert [2, 3, 6, 3, 2] == ar.next_smallest_palindrome_number([2, 3, 5, 4, 5])
        assert [9, 4, 1, 8, 8, 0, 8, 8, 1, 4, 9] == ar.next_smallest_palindrome_number(
            [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2],
        )

    def test_aggressive_cows(self):
        """Test `aggressive_cows`."""
        assert ar.aggressive_cows([1, 2, 4, 8, 9], 3) == 3
        assert ar.aggressive_cows([10, 1, 2, 7, 5], 3) == 4

    def test_smaller_on_right_counts(self):
        """Test `smaller_on_right_counts`."""
        assert [6, 1, 1, 1, 0, 1, 0] == ar.smaller_on_right_counts(
            [12, 1, 2, 3, 0, 11, 4],
        )
        assert [0, 0, 0, 0] == ar.smaller_on_right_counts([1, 2, 3, 4])
        assert [0, 0, 0, 0, 0] == ar.smaller_on_right_counts([1, 2, 3, 4, 5])

        assert [3, 2, 1, 0] == ar.smaller_on_right_counts([4, 3, 2, 1])
        assert [4, 3, 2, 1, 0] == ar.smaller_on_right_counts([5, 4, 3, 2, 1])

    def test_unsorted_pairs_count(self):
        """Test `unsorted_pairs_count`."""
        assert ar.unsorted_pairs_count([12, 1, 2, 3, 0, 11, 4]) == 10
        assert ar.unsorted_pairs_count([1, 2, 3, 4]) == 0
        assert ar.unsorted_pairs_count([1, 2, 3, 4, 5]) == 0
        assert ar.unsorted_pairs_count([4, 3, 2, 1]) == 6
        assert ar.unsorted_pairs_count([5, 4, 3, 2, 1]) == 10

    def test_min_sum_split(self):
        """Test `min_sum_split`."""
        assert ar.min_sum_split([1, 2, 3, 4], 1) == 10
        assert ar.min_sum_split([1, 2, 3, 4], 2) == 6
        assert ar.min_sum_split([1, 2, 3, 4], 3) == 4
        assert ar.min_sum_split([1, 2, 3, 4], 4) == 4

    def test_out_of_there_number(self):
        """Test `out_of_there_number`."""
        assert ar.out_ouf_there_number([2]) == 1
        assert ar.out_ouf_there_number([1, 10, 3]) == 2
        assert ar.out_ouf_there_number([1, 3, 2]) == 7

    def test_max_min_window(self):
        """Test `max_min_window`."""
        assert [70, 30, 20, 10, 10, 10, 10] == ar.max_min_window(
            [10, 20, 30, 50, 10, 70, 30],
        )

    def test_candy(self):
        """Test `candy`."""
        assert ar.candy([1, 0, 1]) == 5
        assert ar.candy([1, 2, 1]) == 4
        assert ar.candy([1, 2, 2]) == 4
        assert ar.candy([1, 2, 3]) == 6
        assert ar.candy([3, 2, 1]) == 6
        assert ar.candy([2, 3, 2, 1]) == 7
        assert ar.candy([3, 2, 3, 2, 1]) == 9

    def test_max_sum_substring(self):
        """Test `max_sum_substring`."""
        assert ar.max_sum_substring("h", {}) == "h"
        assert ar.max_sum_substring("h", {"h": -880}) == "h"
        assert ar.max_sum_substring("oK", {"K": -880}) == "o"
        assert ar.max_sum_substring("abcde", {"c": -880}) == "de"
        d = dict(zip("ZhXg", [342, -625, -904, 451]))
        assert ar.max_sum_substring("h3hkghXZ", d) == "kg"

    def test_zero_sum_sub_max_len(self):
        """Test `zero_sum_sub_max_len`."""
        assert ar.zero_sum_sub_max_len([15, -2, 2, -8, 1, 7, 10, 23]) == 5
        assert ar.zero_sum_sub_max_len([15, -2, 2, -8, 1, 7, 10, -25, 10, 23]) == 8

    def test_zero_sum_sub_max_interval(self):
        """Test `zero_sum_sub_max_interval`."""
        assert ar.zero_sum_sub_max_interval([15, -2, 2, -8, 1, 7, 10, 23]) == (1, 6)
        assert ar.zero_sum_sub_max_interval([15, -2, 2, -8, 1, 7, 10, -25, 10, 23]) == (
            0,
            8,
        )

    def test_max_profit(self):
        """Test `max_profit`."""
        assert ar.max_profit([], 0) == 0
        assert ar.max_profit([], 1) == 0
        assert ar.max_profit([10], 0) == 0
        assert ar.max_profit([10], 1) == 0
        assert ar.max_profit([10, 20], 0) == 0
        assert ar.max_profit([10, 20], 1) == 10
        assert ar.max_profit([10, 20, 5, 10], 1) == 10
        assert ar.max_profit([10, 20, 5, 25], 1) == 20
        assert ar.max_profit([10, 20, 5, 10], 2) == 15
        assert ar.max_profit([10, 20, 5, 25], 2) == 30
        assert ar.max_profit([5, 20, 10, 25], 1) == 20
        assert ar.max_profit([5, 20, 25, 10], 2) == 20
        assert ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 0) == 0
        assert ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 1) == 95
        assert ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 2) == 107
        assert ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 8) == 117
        assert ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 20) == 117

    def test_count_changes_to_make_strict(self):
        """Test `count_changes_to_make_strict`."""
        assert ar.count_changes_to_make_strict([]) == 0
        assert ar.count_changes_to_make_strict([9]) == 0
        assert ar.count_changes_to_make_strict([1, 2]) == 0
        assert ar.count_changes_to_make_strict([2, 1]) == 1
        assert ar.count_changes_to_make_strict([1, 2, 3, 4]) == 0
        assert ar.count_changes_to_make_strict([4, 3, 2, 1]) == 3
        assert ar.count_changes_to_make_strict([1, 2, 3, 6, 5, 4]) == 2
        assert ar.count_changes_to_make_strict([1, 2, 3, 1, 5]) == 1
        assert ar.count_changes_to_make_strict([1, 6, 4, 6, 4]) == 2
        assert ar.count_changes_to_make_strict([7, 7, 5, 3, 3, 9, 5]) == 5
        assert ar.count_changes_to_make_strict([10, 5, 5, 2, 4, 10, 3, 2, 7, 9]) == 7

    def test_repeated_numbers(self):
        """Test `repeated_numbers`."""
        assert not ar.repeated_numbers([])
        assert ar.repeated_numbers([1, 1]) == (1,)
        assert ar.repeated_numbers([1, 2, 1]) == (1,)
        assert ar.repeated_numbers([1, 2, 2]) == (2,)
        assert ar.repeated_numbers([1, 2, 3, 2, 3, 4, 5]) == (2, 3)
        assert ar.repeated_numbers([1, 2, 3, 3, 2, 4, 5]) == (3, 2)

    def test_geek_roads(self):
        """Test `geek_roads`."""
        assert ar.geek_roads([2], [3]) == 3
        assert ar.geek_roads([2, 3, 5], [1, 3, 3, 4]) == 12
        assert ar.geek_roads([4, 5, 6], [1, 5, 7]) == 16
        assert ar.geek_roads([1, 4, 5, 6, 8], [2, 3, 4, 6, 9]) == 29
        assert ar.geek_roads([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]) == 35
        assert ar.geek_roads([1, 4, 5, 8, 8, 8], [2, 8, 9, 9, 9]) == 61
        assert ar.geek_roads([1, 8, 8, 9, 11, 12], [6, 6, 8, 9, 10, 14]) == 61
        assert ar.geek_roads([1, 4, 5, 8, 8, 8], [2, 8, 8, 9, 9, 9]) == 69
        assert ar.geek_roads([4, 5, 6, 7, 8, 8, 9], [1, 1, 8, 8, 8, 8, 8]) == 71
        assert (
            ar.geek_roads(
                [1, 2, 3, 4, 5, 6, 6, 7],
                [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7],
            )
            == 49
        )

    def test_partition_by_sum(self):
        """Test `partition_by_sum`."""
        assert ar.partition_by_sum([]) == (0, 0)
        assert ar.partition_by_sum([2]) == (0, 2)
        assert ar.partition_by_sum([2, 2]) == (2, 2)
        assert ar.partition_by_sum([2, 2, 2]) == (2, 4)
        assert ar.partition_by_sum([2, 2, 2, 2]) == (4, 4)
