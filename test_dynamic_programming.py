"""Test module for the dynamic programming related puzzles."""

import unittest

import dynamic_programming as dp


class TestDP(unittest.TestCase):
    """Test class for the dp related puzzles."""

    def test_stack_boxes(self):
        """Test `stack_boxes`."""
        assert dp.stack_boxes([]) == 0
        assert dp.stack_boxes([(1, 5, 5)]) == 5
        assert dp.stack_boxes([(1, 2, 9), (8, 6, 1)]) == 10
        assert dp.stack_boxes([(1, 2, 3), (4, 5, 6), (3, 4, 1)]) == 15
        assert dp.stack_boxes([(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]) == 60

    def test_prime_product_subset_count(self):
        """Test `prime_product_subset_count`."""
        assert dp.prime_product_subset_count([]) == 0
        assert dp.prime_product_subset_count([1]) == 0
        assert dp.prime_product_subset_count([2]) == 1
        assert dp.prime_product_subset_count([1, 2]) == 2
        assert dp.prime_product_subset_count([10, 4, 1, 4, 10]) == 4
        assert dp.prime_product_subset_count([2, 2, 3]) == 5
        assert dp.prime_product_subset_count([1, 2, 3, 4]) == 6
