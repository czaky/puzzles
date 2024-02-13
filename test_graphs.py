"""Test module for the graph based puzzles."""
import unittest
import graphs as g

class TestGraphs(unittest.TestCase):
    """Test class for the graph based puzzles."""
    def test_breadth_first(self):
        "Test `breadth_first` traversal."
        adj = [[1, 2, 3], [], [4], [], []]
        self.assertEqual([0, 1, 2, 3, 4], g.breadth_first(adj))
