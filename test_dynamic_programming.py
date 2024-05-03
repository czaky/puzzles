"""Test module for the dynamic programming related puzzles."""

import unittest

import dynamic_programming as dp


class TestDP(unittest.TestCase):
    """Test class for the dp related puzzles."""

    def test_stack_boxes(self):
        "Test `stack_boxes`."
        self.assertEqual(0, dp.stack_boxes([]))
        self.assertEqual(5, dp.stack_boxes([(1, 5, 5)]))
        self.assertEqual(10, dp.stack_boxes([(1, 2, 9), (8, 6, 1)]))
        self.assertEqual(15, dp.stack_boxes([(1, 2, 3), (4, 5, 6), (3, 4, 1)]))
        self.assertEqual(
            60, dp.stack_boxes([(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)])
        )

    def test_prime_product_subset_count(self):
        "Test `prime_product_subset_count`."
        self.assertEqual(0, dp.prime_product_subset_count([]))
        self.assertEqual(0, dp.prime_product_subset_count([1]))
        self.assertEqual(1, dp.prime_product_subset_count([2]))
        self.assertEqual(2, dp.prime_product_subset_count([1, 2]))
        self.assertEqual(4, dp.prime_product_subset_count([10, 4, 1, 4, 10]))
        self.assertEqual(5, dp.prime_product_subset_count([2, 2, 3]))
        self.assertEqual(6, dp.prime_product_subset_count([1, 2, 3, 4]))
