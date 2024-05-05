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

    def test_bitonic_point(self):
        "Test `bitonic_point` function."
        self.assertEqual(5, ar.bitonic_point([1, 3, 5]))
        self.assertEqual(5, ar.bitonic_point([1, 3, 5, 4]))
        self.assertEqual(1, ar.bitonic_point([1]))

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

    def test_meta_cafeteria(self):
        "Test `meta_cafeteria` puzzle."
        self.assertEqual(3, ar.meta_cafeteria(10, 1, [2, 6]))
        self.assertEqual(1, ar.meta_cafeteria(15, 2, [11, 6, 14]))

    def test_product_except_self(self):
        "Test `product_except_self`."
        self.assertEqual(
            [0, 0, 0, 1800, 0, 0], ar.product_except_self([10, 3, 5, 0, 6, 2])
        )
        self.assertEqual(
            [180, 600, 360, 300, 900], ar.product_except_self([10, 3, 5, 6, 2])
        )

    def test_count_triplets(self):
        "Test `count_triplets`."
        self.assertEqual(2, ar.count_triplets([1, 5, 3, 2]))
        self.assertEqual(1, ar.count_triplets([10, 3, 5, 6, 2]))

    def test_greater_smaller(self):
        "Validate `greater_smaller` puzzle solution."
        self.assertEqual(11, ar.greater_smaller([10, 6, 3, 1, 5, 11, 6, 1, 11, 12]))
        self.assertIsNone(ar.greater_smaller([10, 6, 3, 1, 5, 13, 6, 1, 11, 12]))
        self.assertIsNone(ar.greater_smaller([10, 6, 3]))
        self.assertIsNone(ar.greater_smaller([6, 3, 10]))

    def test_smallest_sub_with_greater_sum(self):
        "Test `smallest_sub_with_greater_sum` function."
        self.assertEqual(0, ar.smallest_sub_with_greater_sum([255], 333))
        self.assertEqual(1, ar.smallest_sub_with_greater_sum([255], 111))
        self.assertEqual(3, ar.smallest_sub_with_greater_sum([1, 4, 45, 6, 0, 19], 51))
        self.assertEqual(3, ar.smallest_sub_with_greater_sum([1, 4, 3, 6, 42, 4], 51))
        self.assertEqual(3, ar.smallest_sub_with_greater_sum([45, 4, 3, 6, 2, 4], 51))

    def test_window_distinct_count(self):
        "Test `window_distinct_count`."
        self.assertEqual([5, 5], ar.window_distinct_count([10, 3, 5, 0, 6, 2], 5))
        self.assertEqual([2, 2, 2, 2], ar.window_distinct_count([10, 3, 5, 6, 2], 2))
        self.assertEqual(
            [3, 4, 4, 3], ar.window_distinct_count([1, 2, 1, 3, 4, 2, 3], 4)
        )

    def test_find_extra_element(self):
        "Test `find_extra_element` function."
        self.assertEqual(0, ar.find_extra_element([1], []))
        self.assertEqual(1, ar.find_extra_element([1, 2], [1]))
        self.assertEqual(0, ar.find_extra_element([1, 2], [2]))
        self.assertEqual(1, ar.find_extra_element([1], [1, 2]))
        self.assertEqual(0, ar.find_extra_element([2], [1, 2]))
        self.assertEqual(2, ar.find_extra_element([1, 2, 3], [1, 2]))
        self.assertEqual(0, ar.find_extra_element([1, 2, 3], [2, 3]))
        self.assertEqual(2, ar.find_extra_element([1, 2, 3, 4, 5], [1, 2, 4, 5]))

    def test_pascal_triangle_row(self):
        "Test `test_pascal_triangle_row` function."
        self.assertEqual([1], ar.pascal_triangle_row(1))
        self.assertEqual([1, 1], ar.pascal_triangle_row(2))
        self.assertEqual([1, 2, 1], ar.pascal_triangle_row(3))
        self.assertEqual([1, 3, 3, 1], ar.pascal_triangle_row(4))

    def test_min_diff(self):
        "Test `min_diff` function."
        self.assertEqual(4, ar.min_diff([1, 9, 5, 11, 2], 3))
        self.assertEqual(7, ar.min_diff([2, 30, 8, 11, 20, 1, 3], 4))
        self.assertEqual(2, ar.min_diff([1, 7, 3], 2))

    def test_duplicated_sorted_find_unique(self):
        "Test `duplicated_sorted_find_unique` function."
        self.assertEqual(5, ar.duplicated_sorted_find_unique([1, 1, 5, 8, 8]))
        self.assertEqual(1, ar.duplicated_sorted_find_unique([1, 3, 3, 4, 4, 5, 5]))
        self.assertEqual(3, ar.duplicated_sorted_find_unique([1, 1, 3]))

    def test_max_equal_zero_and_one_length(self):
        "Test `max_equal_zero_and_one_length` function."
        self.assertEqual(4, ar.max_equal_zero_and_one_length([1, 0, 1, 0, 1]))
        self.assertEqual(6, ar.max_equal_zero_and_one_length([1, 0, 1, 1, 1, 0, 0]))
        self.assertEqual(2, ar.max_equal_zero_and_one_length([0, 0, 1]))
        self.assertEqual(0, ar.max_equal_zero_and_one_length([0]))
        self.assertEqual(0, ar.max_equal_zero_and_one_length([]))

    def test_toys_with_budget(self):
        "Test `toys_with_budget` function."
        self.assertEqual(4, ar.toys_with_budget([60, 5, 4, 3, 2, 20], 15))
        self.assertEqual(3, ar.toys_with_budget([30, 20, 50], 100))

    def test_first_last(self):
        "Test `first_last` function."
        self.assertEqual((0, 0), ar.first_last([1, 2, 3, 3, 3, 4], 1))
        self.assertEqual((2, 4), ar.first_last([1, 2, 3, 3, 3, 4], 3))
        self.assertEqual((0, 1), ar.first_last([1, 1, 2, 3, 3, 3, 4], 1))
        self.assertEqual((6, 6), ar.first_last([1, 1, 2, 3, 3, 3, 4], 4))
        self.assertEqual((4, 6), ar.first_last([1, 1, 2, 3, 4, 4, 4], 4))
        self.assertEqual((-1, -1), ar.first_last([1, 1, 2, 3, 4, 4, 4], 5))

    def test_merge_sorted(self):
        "Test `merge_sorted` function."
        a = [4, 5, 6, 12, 13]
        b = [0, 7, 8, 13, 12, 15]
        ar.merge_sorted(a, b)
        self.assertEqual([0, 4, 5, 6, 7], a)
        self.assertEqual([8, 12, 12, 13, 13, 15], b)
        a, b = b, a
        ar.merge_sorted(a, b)
        self.assertEqual([0, 4, 5, 6, 7, 8], a)
        self.assertEqual([12, 12, 13, 13, 15], b)

    def test_min_partition_diff(self):
        "Test `min_partition_diff` function."
        self.assertEqual(1, ar.min_partition_diff([1]))
        self.assertEqual(1, ar.min_partition_diff([1, 2]))
        self.assertEqual(1, ar.min_partition_diff([2, 1]))
        self.assertEqual(3, ar.min_partition_diff([5, 2]))
        self.assertEqual(3, ar.min_partition_diff([2, 5]))
        self.assertEqual(26, ar.min_partition_diff([60, 5, 4, 3, 2, 20]))
        self.assertEqual(0, ar.min_partition_diff([30, 20, 50]))

    def test_max_histogram_rectangle(self):
        "Test `max_histogram_rectangle` function."
        self.assertEqual(6, ar.max_histogram_rectangle([6]))
        self.assertEqual(4, ar.max_histogram_rectangle([3, 2]))
        self.assertEqual(4, ar.max_histogram_rectangle([2, 3]))
        self.assertEqual(4, ar.max_histogram_rectangle([3, 2, 1]))
        self.assertEqual(4, ar.max_histogram_rectangle([2, 3, 1]))
        self.assertEqual(4, ar.max_histogram_rectangle([1, 3, 2]))
        self.assertEqual(4, ar.max_histogram_rectangle([1, 2, 3]))
        self.assertEqual(12, ar.max_histogram_rectangle([6, 2, 5, 4, 5, 1, 6]))
        self.assertEqual(7, ar.max_histogram_rectangle([1, 2, 1, 2, 1, 2, 1]))

    def test_median2(self):
        "Test `median2` function."
        self.assertEqual(3, ar.median2([1, 2, 3], [4, 6]))
        self.assertEqual(3.5, ar.median2([1, 2, 3], [4, 5, 6]))

    def test_next_smallest_palindrome(self):
        "Test `next_smallest_palindrome` function."
        self.assertEqual([], ar.next_smallest_palindrome_number([]))
        self.assertEqual([1], ar.next_smallest_palindrome_number([0]))
        self.assertEqual([8], ar.next_smallest_palindrome_number([7]))
        self.assertEqual([1, 1], ar.next_smallest_palindrome_number([9]))
        self.assertEqual([6, 6], ar.next_smallest_palindrome_number([6, 1]))
        self.assertEqual([1, 0, 1], ar.next_smallest_palindrome_number([9, 9]))
        self.assertEqual([2, 4, 4, 2], ar.next_smallest_palindrome_number([2, 3, 4, 5]))
        self.assertEqual(
            [2, 3, 6, 3, 2], ar.next_smallest_palindrome_number([2, 3, 5, 4, 5])
        )
        self.assertEqual(
            [9, 4, 1, 8, 8, 0, 8, 8, 1, 4, 9],
            ar.next_smallest_palindrome_number([9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]),
        )

    def test_aggressive_cows(self):
        "Test `aggressive_cows`."
        self.assertEqual(3, ar.aggressive_cows([1, 2, 4, 8, 9], 3))
        self.assertEqual(4, ar.aggressive_cows([10, 1, 2, 7, 5], 3))

    def test_smaller_on_right_counts(self):
        "Test `smaller_on_right_counts`"
        self.assertEqual(
            [6, 1, 1, 1, 0, 1, 0], ar.smaller_on_right_counts([12, 1, 2, 3, 0, 11, 4])
        )
        self.assertEqual([0, 0, 0, 0], ar.smaller_on_right_counts([1, 2, 3, 4]))
        self.assertEqual([0, 0, 0, 0, 0], ar.smaller_on_right_counts([1, 2, 3, 4, 5]))

        self.assertEqual([3, 2, 1, 0], ar.smaller_on_right_counts([4, 3, 2, 1]))
        self.assertEqual([4, 3, 2, 1, 0], ar.smaller_on_right_counts([5, 4, 3, 2, 1]))

    def test_unsorted_pairs_count(self):
        "Test `unsorted_pairs_count`"
        self.assertEqual(10, ar.unsorted_pairs_count([12, 1, 2, 3, 0, 11, 4]))
        self.assertEqual(0, ar.unsorted_pairs_count([1, 2, 3, 4]))
        self.assertEqual(0, ar.unsorted_pairs_count([1, 2, 3, 4, 5]))
        self.assertEqual(6, ar.unsorted_pairs_count([4, 3, 2, 1]))
        self.assertEqual(10, ar.unsorted_pairs_count([5, 4, 3, 2, 1]))

    def test_min_sum_split(self):
        "Test `min_sum_split`."
        self.assertEqual(10, ar.min_sum_split([1, 2, 3, 4], 1))
        self.assertEqual(6, ar.min_sum_split([1, 2, 3, 4], 2))
        self.assertEqual(4, ar.min_sum_split([1, 2, 3, 4], 3))
        self.assertEqual(4, ar.min_sum_split([1, 2, 3, 4], 4))

    def test_out_of_there_number(self):
        "Test `out_of_there_number`."
        self.assertEqual(1, ar.out_ouf_there_number([2]))
        self.assertEqual(2, ar.out_ouf_there_number([1, 10, 3]))
        self.assertEqual(7, ar.out_ouf_there_number([1, 3, 2]))

    def test_max_min_window(self):
        "Test `max_min_window`."
        self.assertEqual(
            [70, 30, 20, 10, 10, 10, 10],
            ar.max_min_window([10, 20, 30, 50, 10, 70, 30]),
        )

    def test_candy(self):
        "Test `candy`."
        self.assertEqual(5, ar.candy([1, 0, 1]))
        self.assertEqual(4, ar.candy([1, 2, 1]))
        self.assertEqual(4, ar.candy([1, 2, 2]))
        self.assertEqual(6, ar.candy([1, 2, 3]))
        self.assertEqual(6, ar.candy([3, 2, 1]))
        self.assertEqual(7, ar.candy([2, 3, 2, 1]))
        self.assertEqual(9, ar.candy([3, 2, 3, 2, 1]))

    def test_max_sum_substring(self):
        "Test `max_sum_substring`."
        self.assertEqual("h", ar.max_sum_substring("h", {}))
        self.assertEqual("h", ar.max_sum_substring("h", {"h": -880}))
        self.assertEqual("o", ar.max_sum_substring("oK", {"K": -880}))
        self.assertEqual("de", ar.max_sum_substring("abcde", {"c": -880}))
        d = dict(zip("ZhXg", [342, -625, -904, 451]))
        self.assertEqual("kg", ar.max_sum_substring("h3hkghXZ", d))

    def test_zero_sum_sub_max_len(self):
        "Test `zero_sum_sub_max_len`."
        self.assertEqual(5, ar.zero_sum_sub_max_len([15, -2, 2, -8, 1, 7, 10, 23]))
        self.assertEqual(
            8, ar.zero_sum_sub_max_len([15, -2, 2, -8, 1, 7, 10, -25, 10, 23])
        )

    def test_zero_sum_sub_max_interval(self):
        "Test `zero_sum_sub_max_interval`."
        self.assertEqual(
            (1, 6), ar.zero_sum_sub_max_interval([15, -2, 2, -8, 1, 7, 10, 23])
        )
        self.assertEqual(
            (0, 8), ar.zero_sum_sub_max_interval([15, -2, 2, -8, 1, 7, 10, -25, 10, 23])
        )

    def test_max_profit(self):
        "Test `max_profit`."
        self.assertEqual(0, ar.max_profit([], 0))
        self.assertEqual(0, ar.max_profit([], 1))
        self.assertEqual(0, ar.max_profit([10], 0))
        self.assertEqual(0, ar.max_profit([10], 1))
        self.assertEqual(0, ar.max_profit([10, 20], 0))
        self.assertEqual(10, ar.max_profit([10, 20], 1))
        self.assertEqual(10, ar.max_profit([10, 20, 5, 10], 1))
        self.assertEqual(20, ar.max_profit([10, 20, 5, 25], 1))
        self.assertEqual(15, ar.max_profit([10, 20, 5, 10], 2))
        self.assertEqual(30, ar.max_profit([10, 20, 5, 25], 2))
        self.assertEqual(20, ar.max_profit([5, 20, 10, 25], 1))
        self.assertEqual(20, ar.max_profit([5, 20, 25, 10], 2))
        self.assertEqual(0, ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 0))
        self.assertEqual(95, ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 1))
        self.assertEqual(107, ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 2))
        self.assertEqual(117, ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 8))
        self.assertEqual(117, ar.max_profit([10, 22, 5, 75, 65, 80, 90, 100], 20))

    def test_count_changes_to_make_strict(self):
        "Test `count_changes_to_make_strict`."
        self.assertEqual(0, ar.count_changes_to_make_strict([]))
        self.assertEqual(0, ar.count_changes_to_make_strict([9]))
        self.assertEqual(0, ar.count_changes_to_make_strict([1, 2]))
        self.assertEqual(1, ar.count_changes_to_make_strict([2, 1]))
        self.assertEqual(0, ar.count_changes_to_make_strict([1, 2, 3, 4]))
        self.assertEqual(3, ar.count_changes_to_make_strict([4, 3, 2, 1]))
        self.assertEqual(2, ar.count_changes_to_make_strict([1, 2, 3, 6, 5, 4]))
        self.assertEqual(1, ar.count_changes_to_make_strict([1, 2, 3, 1, 5]))
        self.assertEqual(2, ar.count_changes_to_make_strict([1, 6, 4, 6, 4]))
        self.assertEqual(5, ar.count_changes_to_make_strict([7, 7, 5, 3, 3, 9, 5]))
        self.assertEqual(
            7, ar.count_changes_to_make_strict([10, 5, 5, 2, 4, 10, 3, 2, 7, 9])
        )

    def test_repeated_numbers(self):
        "Test `repeated_numbers`."
        self.assertEqual((), ar.repeated_numbers([]))
        self.assertEqual((1,), ar.repeated_numbers([1, 1]))
        self.assertEqual((1,), ar.repeated_numbers([1, 2, 1]))
        self.assertEqual((2,), ar.repeated_numbers([1, 2, 2]))
        self.assertEqual((2, 3), ar.repeated_numbers([1, 2, 3, 2, 3, 4, 5]))
        self.assertEqual((3, 2), ar.repeated_numbers([1, 2, 3, 3, 2, 4, 5]))

    def test_geek_roads(self):
        "Test `geek_roads`."
        self.assertEqual(3, ar.geek_roads([2], [3]))
        self.assertEqual(12, ar.geek_roads([2, 3, 5], [1, 3, 3, 4]))
        self.assertEqual(16, ar.geek_roads([4, 5, 6], [1, 5, 7]))
        self.assertEqual(29, ar.geek_roads([1, 4, 5, 6, 8], [2, 3, 4, 6, 9]))
        self.assertEqual(35, ar.geek_roads([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]))
        self.assertEqual(61, ar.geek_roads([1, 4, 5, 8, 8, 8], [2, 8, 9, 9, 9]))
        self.assertEqual(61, ar.geek_roads([1, 8, 8, 9, 11, 12], [6, 6, 8, 9, 10, 14]))
        self.assertEqual(69, ar.geek_roads([1, 4, 5, 8, 8, 8], [2, 8, 8, 9, 9, 9]))
        self.assertEqual(
            71, ar.geek_roads([4, 5, 6, 7, 8, 8, 9], [1, 1, 8, 8, 8, 8, 8])
        )
        self.assertEqual(
            49,
            ar.geek_roads(
                [1, 2, 3, 4, 5, 6, 6, 7], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7]
            ),
        )

    def test_partition_by_sum(self):
        "Test `partition_by_sum`."
        self.assertEqual((0, 0), ar.partition_by_sum([]))
        self.assertEqual((0, 2), ar.partition_by_sum([2]))
        self.assertEqual((2, 2), ar.partition_by_sum([2, 2]))
        self.assertEqual((2, 4), ar.partition_by_sum([2, 2, 2]))
        self.assertEqual((4, 4), ar.partition_by_sum([2, 2, 2, 2]))
