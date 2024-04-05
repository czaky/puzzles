"""Test module for the graph based puzzles."""

import unittest
import graphs as g


class TestGraphs(unittest.TestCase):
    """Test class for the graph based puzzles."""

    def test_breadth_first(self):
        "Test `breadth_first` traversal."
        adj = [[1, 2, 3], [], [4], [], []]
        self.assertEqual([0, 1, 2, 3, 4], g.breadth_first(adj))

    def test_depth_first(self):
        "Test `depth_first` traversal."
        adj = [[1, 2, 3], [], [4], [], []]
        self.assertEqual([0, 1, 2, 4, 3], g.depth_first(adj))

    def test_circle_of_words(self):
        "Test `circle_of_words`."
        self.assertTrue(g.circle_of_words(["abc", "cde", "eda"]))
        self.assertFalse(g.circle_of_words(["abc", "cde", "edf"]))

    def test_articulation_points(self):
        "Test `articulation_points`."
        self.assertEqual(
            [1, 4], g.articulation_points([[1], [0, 4], [3, 4], [2, 4], [1, 2, 3]])
        )

    def test_critical_connections(self):
        "Test `critical_connections`."
        self.assertEqual([(0, 1), (0, 2)], g.critical_connections([[1, 2], [0], [0]]))
        self.assertEqual(
            [(2, 3)], g.critical_connections([[1, 2], [0, 2], [0, 1, 3], [2]])
        )
