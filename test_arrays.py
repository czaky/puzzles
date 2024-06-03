"""Test module for the array/list related puzzles."""

import operator as op
import unittest

import arrays as ar


class TestRotatedArray(unittest.TestCase):
    """Test class for sorted, rotated array puzzles."""


class TestUnsortedArray(unittest.TestCase):
    """Test class for unsorted array puzzles."""

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
            [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2]
        )

    def test_aggressive_cows(self):
        """Test `aggressive_cows`."""
        assert ar.aggressive_cows([1, 2, 4, 8, 9], 3) == 3
        assert ar.aggressive_cows([10, 1, 2, 7, 5], 3) == 4

    def test_smaller_on_right_counts(self):
        """Test `smaller_on_right_counts`."""
        assert [6, 1, 1, 1, 0, 1, 0] == ar.smaller_on_right_counts(
            [12, 1, 2, 3, 0, 11, 4]
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
            [10, 20, 30, 50, 10, 70, 30]
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
                [1, 2, 3, 4, 5, 6, 6, 7], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7]
            )
            == 49
        )

    def test_next_element(self):
        """Test `next_element`."""
        assert ar.next_element(op.gt, [1, 3, 2, 4], -1) == [3, 4, 4, -1]
        assert ar.next_element(op.gt, [1, 3, 4, 5], -1) == [3, 4, 5, -1]
        assert ar.next_element(op.gt, [6, 3, 4, 5], -1) == [-1, 4, 5, -1]

    def test_geeky_132_buildings(self):
        """Test geeky_132_buildings."""
        assert ar.geeky_132_buildings([2, 5, 4, 3, 1])
        assert ar.geeky_132_buildings([2, 4, 1, 5, 3])
        assert ar.geeky_132_buildings([13821, 30190, 3293, 20731])
        assert ar.geeky_132_buildings([4, 17, 11, 5, 13, 2])
        assert not ar.geeky_132_buildings([11, 11, 12, 9])
        assert not ar.geeky_132_buildings([11, 11, 11])
        assert not ar.geeky_132_buildings([11, 13, 11])
        assert not ar.geeky_132_buildings([12, 13, 11])
        assert not ar.geeky_132_buildings([14, 13, 11])
        assert not ar.geeky_132_buildings([12, 13, 14])
        assert ar.geeky_132_buildings([11, 13, 12])
        assert ar.geeky_132_buildings([11, 13, 16, 12])
        assert ar.geeky_132_buildings([11, 13, 10, 12])
        assert ar.geeky_132_buildings([11, 16, 13, 12])
        assert ar.geeky_132_buildings([11, 10, 13, 12])
        assert ar.geeky_132_buildings([11, 10, 13, 16, 12])
        assert ar.geeky_132_buildings([11, 16, 13, 10, 12])

    def test_find_smallest_max_diff_with_inserts(self):
        f = ar.find_smallest_max_diff_with_inserts
        assert f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == 0.5
        assert f([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2) == 14.0

        astr = """74 284 316 461 485 587 589 731 755 843 881 943 1065 1183 1185 1305 1347
        1362 1467 1515 1637 1836 2106 2296 2382 3096 3301 3394 3397 3557 3563 3592 3643
        4057 4084 4101 4176 4204 4218 4226 4321 4511 4595 4770 4829 4831 4856 4984 5019
        5026 5032 5039 5052 5167 5215 5266 5283 5289 5362 5475 5538 5655 5661 5895 6214
        6297 6309 6363 6513 6670 6688 6696 6814 6838 6920 6956 7061 7272 7400 7428 7517
        7549 7622 7878 7996 8141 8164 8328 8340 8381 8390 8412 8454 8476 8553 8606 8763
        8783 8825 8881 8939 8998 9022 9120 9127 9206 9240 9309 9326 9339 9514 9561 9732
        9772 10142 10208 10319 10354 10452 10475 10506 10515 10515 10527 10613 10640
        10640 10647 10795 10802 10864 10924 10951 10952 11027 11054 11078 11130 11140
        11176 11286 11392 11394 11469 11739 11817 11823 11863 11878 11892 11904 11934
        12248 12323 12454 12630 12765 12780 13163 13169 13209 13310 13426 13490 13499
        13535 13539 13648 13790 13838 13968 14019 14118 14180 14197 14300 14341 14474
        14561 14592 14839 14906 15025 15300 15304 15360 15456 15501 15525 15530 15559
        15749 15801 15883 15956 16122 16136 16183 16307 16326 16371 16476 16592 16755
        16858 16862 16887 16899 16915 16917 16930 16965 16974 17031 17036 17097 17239
        17261 17332 17344 17435 17512 17523 17617 17726 17734 17763 18103 18114 18121
        18211 18215 18352 18506 18603 18628 18965 19216 19515 19534 19672 19701 19788
        19864 20004 20103 20105 20134 20318 20496 20618 20621 20740 20858 21018 21024
        21029 21102 21230 21415 21531 21565 21575 21698 21800 21890 21935 21938 21972
        21986 22057 22077 22620 22741 22771 22920 23051 23267 23438 23514 23540 23608
        23743 23907 23919 24000 24046 24131 24159 24201 24452 24458 24466 24633 24734
        24779 24875 24946 25001 25020 25023 25113 25150 25330 25375 25405 25422 25462
        25469 25521 25525 25837 25908 25947 26043 26065 26068 26098 26113 26308 26350
        26459 26490 26571 26809 26873 26941 26973 27096 27134 27156 27342 27402 27534
        27546 27594 27610 27692 27773 27988 28136 28260 28268 28290 28391 28428 28462
        28909 28924 29083 29178 29226 29242 29250 29387 29425 29693 29740 29745 29775
        29786 30097 30132 30294 30377 30497 30726 30829 30841 30843 30886 30980 30994
        31038 31082 31088 31088 31243 31379 31524 31544 31549 31597 31655 31784 31870
        31947 31961 32048 32049 32146 32206 32327 32453 32612 32664 32701 32712"""
        a = list(map(int, astr.split()))
        assert f(a, 26214) == 1.24
        astr = """47 68 92 98 116 119 147 175 191 204 210 290 334 374 404 435 469 487
        493 521 533 547 563 710 711 781 841 848 913 914 920 935 947 960 972 981 1018
        1068 1077 1129 1191 1275 1306 1332 1357 1382 1483 1483 1561 1574 1611 1662 1671
        1676 1693 1703 1723 1727 1762 1824 1856 1876 1879 1899 1948 1993 1994 1995 2001
        2055 2124 2153 2174 2177 2188 2190 2207 2229 2229 2308 2327 2336 2388 2390 2416
        2473 2486 2550 2569 2587 2593 2603 2622 2637 2650 2728 2731 2761 2774 2789 2831
        2836 2899 2915 2932 2958 3020 3099 3138 3143 3166 3176 3201 3217 3305 3310 3313
        3316 3343 3348 3356 3388 3450 3471 3476 3484 3491 3491 3507 3572 3611 3617 3635
        3640 3740 3780 3804 3819 3872 3912 3912 3918 3920 3931 3960 4065 4167 4233 4238
        4244 4344 4544 4549 4611 4650 4709 4715 4720 4761 4798 4800 4826 4854 4864 4866
        4903 4940 4982 4999 5012 5063 5102 5158 5262 5287 5307 5422 5454 5476 5485 5514
        5535 5612 5634 5712 5767 5800 5938 5942 5958 5980 5999 6001 6021 6044 6076 6096
        6144 6202 6221 6272 6289 6377 6459 6459 6460 6549 6635 6725 6749 6782 6784 6809
        6872 6922 6948 6986 7060 7096 7103 7106 7155 7213 7239 7241 7242 7247 7276 7294
        7313 7346 7389 7428 7474 7613 7636 7707 7746 7763 7770 7862 7916 7923 7928 7940
        7947 7979 8025 8152 8184 8204 8212 8239 8247 8291 8296 8332 8353 8386 8408 8413
        8438 8448 8510 8578 8595 8637 8714 8826 8840 8852 8853 8937 9033 9052 9071 9103
        9110 9135 9154 9154 9189 9220 9236 9243 9269 9307 9310 9359 9372 9453 9462 9488
        9523 9539 9607 9630 9671 9707 9743 9781 9850 9956 9994 10017 10020 10060 10061
        10070 10077 10124 10132 10192 10222 10305 10313 10317 10413 10498 10535 10581
        10595 10599 10629 10638 10655 10667 10769 10829 10873 10883 10884 10951 10966
        11025 11030 11074 11124 11187 11201 11216 11244 11274 11350 11384 11462 11486
        11500 11543 11570 11612 11644 11649 11686 11704 11706 11765 11804 11811 11813
        11825 11873 11896 11941 12087 12109 12139 12171 12266 12278 12302 12340 12358
        12366 12377 12383 12386 12396 12410 12444 12466 12472 12513 12535 12535 12547
        12642 12644 12648 12659 12758 12783 12808 12837 12841 12853 12862 12873 12888
        12889 12908 12961 12977 12992 13009 13050 13063 13094 13131 13139 13142 13161
        13187 13188 13220 13239 13256 13267 13378 13425 13427 13488 13532 13533 13570
        13654 13662 13698 13712 13715 13731 13775 13797 13820 13843 13905 13970 14023
        14053 14058 14193 14215 14306 14318 14358 14413 14420 14426 14479 14531 14535
        14561 14564 14627 14663 14691 14880 14901 14904 14930 14935 14977 14993 15009
        15072 15080 15092 15112 15129 15156 15201 15231 15279 15301 15328 15356 15364
        15368 15372 15415 15432 15437 15520 15545 15615 15619 15709 15724 15744 15791
        15802 15815 15815 15837 15876 15919 15937 15968 15980 16018 16019 16039 16047
        16149 16171 16240 16243 16267 16336 16343 16453 16481 16526 16532 16564 16572
        16677 16740 16821 16838 16945 16951 16956 17061 17096 17125 17179 17193 17204
        17225 17269 17286 17295 17501 17537 17538 17578 17627 17664 17737 17784 17812
        17844 17849 17854 17856 17935 17962 17969 17984 18031 18119 18137 18211 18302
        18322 18332 18374 18410 18505 18513 18519 18546 18640 18641 18658 18682 18694
        18742 18811 18832 18839 18870 18905 18908 18968 18979 18999 19018 19032 19067
        19075 19088 19215 19283 19334 19359 19418 19451 19505 19514 19533 19533 19544
        19631 19655 19750 19812 19824 19830 19836 19863 19871 19925 19948 19958 19958
        20023 20094 20129 20131 20191 20196 20211 20287 20294 20329 20457 20469 20475
        20525 20540 20564 20632 20647 20659 20761 20766 20782 20841 20868 20882 20961
        20965 21024 21029 21065 21088 21104 21133 21143 21153 21209 21211 21211 21239
        21278 21288 21289 21386 21393 21414 21453 21453 21458 21473 21491 21500 21576
        21640 21670 21699 21720 21722 21751 21813 21827 21831 21832 21892 21922 21936
        21953 22020 22021 22066 22071 22096 22105 22239 22246 22252 22277 22305 22335
        22361 22392 22393 22403 22440 22477 22562 22596 22613 22616 22639 22658 22693
        22712 22738 22847 22876 22891 22892 22893 22911 23015 23066 23150 23273 23382
        23401 23471 23493 23594 23630 23711 23719 23777 23814 23829 23834 23835 23844
        23901 23932 23934 23942 23964 24016 24030 24068 24100 24115 24186 24210 24224
        24282 24289 24301 24319 24374 24427 24427 24460 24485 24487 24610 24639 24673
        24708 24748 24761 24806 24849 24856 24887 24937 24944 25002 25082 25109 25144
        25168 25286 25287 25320 25326 25357 25405 25456 25476 25571 25584 25774 25780
        25835 25860 25867 25872 25884 25975 26079 26184 26197 26240 26305 26314 26356
        26360 26410 26451 26455 26456 26459 26462 26488 26489 26514 26566 26577 26670
        26702 26738 26740 26745 26748 26820 26840 26844 26871 26947 26951 27015 27016
        27040 27105 27116 27164 27166 27175 27233 27244 27322 27370 27430 27435 27454
        27461 27493 27525 27532 27582 27602 27609 27631 27650 27681 27690 27697 27697
        27737 27747 27876 27899 27912 27971 27985 28005 28084 28125 28252 28310 28388
        28437 28460 28463 28498 28540 28557 28704 28744 28826 28926 28999 28999 29013
        29013 29023 29083 29095 29141 29147 29200 29262 29291 29295 29302 29386 29388
        29404 29466 29496 29498 29624 29624 29690 29724 29730 29763 29901 29901 30046
        30048 30100 30148 30202 30241 30243 30338 30386 30408 30417 30439 30444 30459
        30484 30492 30525 30525 30541 30698 30704 30748 30757 30805 30837 30918 30939
        30960 30987 30998 31013 31045 31099 31122 31149 31154 31237 31243 31287 31332
        31361 31375 31378 31379 31389 31484 31496 31513 31522 31567 31615 31629 31631
        31666 31800 31810 31819 31829 31982 31992 32011 32030 32037 32055 32055 32129
        32156 32158 32174 32174 32226 32264 32300 32425 32435 32457 32477 32559 32567
        32568 32573 32645 32656 32732 32743 32754"""
        a = list(map(int, astr.split()))
        assert f(a, 4138) == 7.0
