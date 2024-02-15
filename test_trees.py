"""Test module for the tree based puzzles."""
import unittest
import trees as t

class TestTrees(unittest.TestCase):
    """Test class for the tree based puzzles."""

    def test_make(self):
        "Test tree make."
        r = t.make("1 2 -1 -1 3")
        self.assertEqual(1, r.data)
        self.assertEqual(2, r.left.data)
        self.assertEqual(3, r.right.data)

    def test_is_bst(self):
        "Test the `is_bst` function."
        self.assertTrue(t.is_bst(t.make("1 -1 -1")))
        self.assertFalse(t.is_bst(t.make("1 2 -1 -1 3")))
        self.assertTrue(t.is_bst(t.make("2 1 -1 -1 3")))
        self.assertFalse(t.is_bst(t.make("2 3 -1 -1 1")))

    def test_left_view(self):
        "Test the `left_view` function."
        self.assertEqual([1], t.left_view(t.make('1')))
        self.assertEqual([1, 2, 3], t.left_view(t.make('1 2 3')))
        self.assertEqual([1, 2], t.left_view(t.make('1 2 -1 -1 3')))
        self.assertEqual([1, 2, 4], t.left_view(t.make('1 2 -1 -1 3 4')))

    def test_balanced(self):
        "Test the `balanced` function."
        self.assertTrue(t.balanced(t.make('1')))
        self.assertFalse(t.balanced(t.make('1 2 3')))
        self.assertTrue(t.balanced(t.make('1 2 -1 -1 3')))
        self.assertFalse(t.balanced(t.make('1 2 -1 -1 3 4 5')))

    def test_identical(self):
        "Test the `identical` function."
        self.assertTrue(t.identical(t.make('1'), t.make('1')))
        self.assertFalse(t.identical(t.make('1'), t.make('1 2 3')))
        self.assertTrue(
            t.identical(t.make('1 2 -1 -1 3'), t.make('1 2 -1 -1 3')))
        self.assertFalse(
            t.identical(
                t.make('1 2 -1 -1 3'),
                t.make('1 2 -1 -1 3 4 5')))

    def test_breadth_first(self):
        "Test `breadth_first` enumeration."
        self.assertEqual([1], t.breadth_first(t.make('1')))
        self.assertEqual([1, 2, 3], t.breadth_first(t.make('1 2 3')))
        self.assertEqual([1, 2, 3], t.breadth_first(t.make('1 2 -1 -1 3')))
        self.assertEqual(
            [1, 2, 3, 4],
            t.breadth_first(t.make('1 2 -1 4 -1 -1 3')))

    def test_iter(self):
        "Test the level order iterator."
        self.assertEqual([1], list(t.make('1')))
        self.assertEqual([2, 1, 3], list(t.make('2 1 3')))
        self.assertEqual(
            [3, 1, 2], list(t.make('3 1 -1 -1 2')))
        self.assertEqual(
            [5, 3, 2, 4], list(t.make('5 3 -1 4 -1 -1 2')))

    def test_insert(self):
        "Test `insert` function."
        self.assertEqual([1, 2], list(t.insert(t.make('1'), 2)))
        self.assertEqual(
            [2, 1, 3], list(t.insert(t.make('2 1 -1 -1 3'), 3)))
        self.assertEqual(
            [2, 1, 3, 4], list(t.insert(t.make('2 1 -1 -1 3'), 4)))
        self.assertEqual(
            [5, 3, 6, 2, 4], list(t.insert(t.make('5 3 -1 4 -1 -1 6'), 2)))
