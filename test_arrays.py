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
            [0, 0, 0, 1800, 0, 0],
            ar.product_except_self([10, 3, 5, 0, 6, 2]))
        self.assertEqual(
            [180, 600, 360, 300, 900],
            ar.product_except_self([10, 3, 5, 6, 2]))

    def test_count_triplets(self):
        "Test `count_triplets`."
        self.assertEqual(2, ar.count_triplets([1, 5, 3, 2]))
        self.assertEqual(1, ar.count_triplets([10, 3, 5, 6, 2]))

    def test_greater_smaller(self):
        "Validate `greater_smaller` puzzle solution."
        self.assertEqual(
            11, ar.greater_smaller([10, 6, 3, 1, 5, 11, 6, 1, 11, 12]))
        self.assertIsNone(
            ar.greater_smaller([10, 6, 3, 1, 5, 13, 6, 1, 11, 12]))
        self.assertIsNone(ar.greater_smaller([10, 6, 3]))
        self.assertIsNone(ar.greater_smaller([6, 3, 10]))

    def test_smallest_sub_with_greater_sum(self):
        "Test `smallest_sub_with_greater_sum` function."
        self.assertEqual(0, ar.smallest_sub_with_greater_sum([255], 333))
        self.assertEqual(1, ar.smallest_sub_with_greater_sum([255], 111))
        self.assertEqual(
            3, ar.smallest_sub_with_greater_sum([1, 4, 45, 6, 0, 19], 51))
        self.assertEqual(
            3, ar.smallest_sub_with_greater_sum([1, 4, 3, 6, 42, 4], 51))
        self.assertEqual(
            3, ar.smallest_sub_with_greater_sum([45, 4, 3, 6, 2, 4], 51))

    def test_window_distinct_count(self):
        "Test `window_distinct_count`."
        self.assertEqual(
            [5, 5],
            ar.window_distinct_count([10, 3, 5, 0, 6, 2], 5))
        self.assertEqual(
            [2, 2, 2, 2],
            ar.window_distinct_count([10, 3, 5, 6, 2], 2))
        self.assertEqual(
            [3, 4, 4, 3],
            ar.window_distinct_count([1, 2, 1, 3, 4, 2, 3], 4))

    def test_find_extra_element(self):
        "Test `find_extra_element` function."
        self.assertEqual(0, ar.find_extra_element([1], []))
        self.assertEqual(1, ar.find_extra_element([1, 2], [1]))
        self.assertEqual(0, ar.find_extra_element([1, 2], [2]))
        self.assertEqual(1, ar.find_extra_element([1], [1, 2]))
        self.assertEqual(0, ar.find_extra_element([2], [1, 2]))
        self.assertEqual(2, ar.find_extra_element([1, 2, 3], [1, 2]))
        self.assertEqual(0, ar.find_extra_element([1, 2, 3], [2, 3]))
        self.assertEqual(
            2, ar.find_extra_element([1, 2, 3, 4, 5], [1, 2, 4, 5]))

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
        self.assertEqual(
            5, ar.duplicated_sorted_find_unique([1, 1, 5, 8, 8]))
        self.assertEqual(
            1, ar.duplicated_sorted_find_unique([1, 3, 3, 4, 4, 5, 5]))
        self.assertEqual(
            3, ar.duplicated_sorted_find_unique([1, 1, 3]))

class TestRotatedArray2(unittest.TestCase):
    """Test class for sorted, rotated array puzzles."""
    def test_max_equal_zero_and_one_length(self):
        "Test `max_equal_zero_and_one_length` function."
        self.assertEqual(
            4, ar.max_equal_zero_and_one_length([1, 0, 1, 0, 1]))
        self.assertEqual(
            6, ar.max_equal_zero_and_one_length([1, 0, 1, 1, 1, 0, 0]))
        self.assertEqual(
            2, ar.max_equal_zero_and_one_length([0, 0, 1]))
        self.assertEqual(
            0, ar.max_equal_zero_and_one_length([0]))
        self.assertEqual(
            0, ar.max_equal_zero_and_one_length([]))

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

    def test_merge(self):
        "Test `merge` function."
        a = [4, 5, 6, 12, 13]
        b = [0, 7, 8, 13, 12, 15]
        ar.merge(a, b)
        self.assertEqual([0, 4,  5,  6,  7], a)
        self.assertEqual([8, 12, 12, 13, 13, 15], b)
        a,b = b,a
        ar.merge(a, b)
        self.assertEqual([0, 4,  5,  6,  7, 8], a)
        self.assertEqual([12, 12, 13, 13, 15], b)

    def test_min_partition_diff(self):
        "Test `min_partition_diff` function."
        self.assertEqual(1, ar.min_partition_diff([1]))
        self.assertEqual(1, ar.min_partition_diff([1, 2]))
        self.assertEqual(1, ar.min_partition_diff([2, 1]))
        self.assertEqual(3, ar.min_partition_diff([5, 2]))
        self.assertEqual(3, ar.min_partition_diff([2, 5]))
        self.assertEqual(26 , ar.min_partition_diff([60, 5, 4, 3, 2, 20]))
        self.assertEqual(0, ar.min_partition_diff([30, 20, 50]))
