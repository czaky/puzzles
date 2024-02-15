"""Test module for the numbers related puzzles."""
import unittest
import mathematics as m

class TestNumbers(unittest.TestCase):
    """Test class for the numbers puzzles."""
    def test_floor_sqrt(self):
        "Test the `floor_sqrt` function."
        self.assertEqual(0, m.floor_sqrt(0))
        self.assertEqual(1, m.floor_sqrt(1))
        self.assertEqual(1, m.floor_sqrt(2))
        self.assertEqual(1, m.floor_sqrt(3))
        self.assertEqual(2, m.floor_sqrt(4))
        self.assertEqual(2, m.floor_sqrt(5))
        self.assertEqual(2, m.floor_sqrt(6))
