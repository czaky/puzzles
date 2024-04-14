"""Test module for the graph based puzzles."""

import unittest
import sets as s


class TestSets(unittest.TestCase):
    """Test class for the set based puzzles."""

    def test_weighted_paths_in_tree(self):
        "Test `weighted_paths_in_tree`."
        self.assertEqual([1], s.weighted_paths_in_tree([[1, 2, 1], [2, 3, 4]], [3]))
        self.assertEqual(
            [1, 3, 4],
            s.weighted_paths_in_tree(
                [[1, 2, 3], [2, 3, 1], [2, 4, 9], [3, 6, 7], [3, 5, 8], [5, 7, 4]],
                [1, 3, 5],
            ),
        )
        self.assertEqual(
            [6, 6, 3, 0, 3, 0, 6, 0, 6],
            s.weighted_paths_in_tree(
                [(3, 1, 3), (4, 2, 2), (3, 4, 1)], [3, 3, 2, 0, 2, 0, 3, 0, 3]
            ),
        )
