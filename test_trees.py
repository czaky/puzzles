"""Test module for the tree based puzzles."""

from typing import Optional, Iterable, Sequence
import unittest
import trees as t


def seq(sequence: Optional[Iterable]) -> Sequence:
    "Return a list out of None | Iterable."
    return list(sequence or [])


class TestTrees(unittest.TestCase):
    """Test class for the tree based puzzles."""

    def test_make_df(self):
        "Test tree make."
        r = t.make_df("1 2 N N 3")
        self.assertEqual(1, r.data)
        self.assertEqual(2, r.left.data)
        self.assertEqual(3, r.right.data)

    def test_is_bst(self):
        "Test the `is_bst` function."
        self.assertTrue(t.is_bst(t.make_df("1 N N")))
        self.assertFalse(t.is_bst(t.make_df("1 2 N N 3")))
        self.assertTrue(t.is_bst(t.make_df("2 1 N N 3")))
        self.assertFalse(t.is_bst(t.make_df("2 3 N N 1")))

    def test_left_view(self):
        "Test the `left_view` function."
        self.assertEqual([1], t.left_view(t.make_df("1")))
        self.assertEqual([1, 2, 3], t.left_view(t.make_df("1 2 3")))
        self.assertEqual([1, 2], t.left_view(t.make_df("1 2 N N 3")))
        self.assertEqual([1, 2, 4], t.left_view(t.make_df("1 2 N N 3 4")))

    def test_balanced(self):
        "Test the `balanced` function."
        self.assertTrue(t.balanced(t.make_df("1")))
        self.assertFalse(t.balanced(t.make_df("1 2 3")))
        self.assertTrue(t.balanced(t.make_df("1 2 N N 3")))
        self.assertFalse(t.balanced(t.make_df("1 2 N N 3 4 5")))

    def test_identical(self):
        "Test the `identical` function."
        self.assertTrue(t.identical(t.make_df("1"), t.make_df("1")))
        self.assertFalse(t.identical(t.make_df("1"), t.make_df("1 2 3")))
        self.assertTrue(t.identical(t.make_df("1 2 N N 3"), t.make_df("1 2 N N 3")))
        self.assertFalse(
            t.identical(t.make_df("1 2 N N 3"), t.make_df("1 2 N N 3 4 5"))
        )

    def test_symmetric(self):
        "Test the `symmetric` function."
        self.assertTrue(t.symmetric(t.make_df("1")))
        self.assertFalse(t.symmetric(t.make_df("1 2 3")))
        self.assertTrue(t.symmetric(t.make_df("1 2 N N 2")))
        self.assertFalse(t.symmetric(t.make_df("1 2 N N 2 2 2")))

    def test_flat(self):
        "Test the `flat` function."
        self.assertTrue(t.flat(t.make_df("1")))
        self.assertTrue(t.flat(t.make_df("1 2 3")))
        self.assertTrue(t.flat(t.make_df("2 1 N N 2")))
        self.assertFalse(t.flat(t.make_df("1 2 N N 3 4 5")))

    def test_breadth_first(self):
        "Test `breadth_first` enumeration."
        self.assertEqual([1], t.breadth_first(t.make_df("1")))
        self.assertEqual([1, 2, 3], t.breadth_first(t.make_df("1 2 3")))
        self.assertEqual([1, 2, 3], t.breadth_first(t.make_df("1 2 N N 3")))
        self.assertEqual([1, 2, 3, 4], t.breadth_first(t.make_df("1 2 N 4 N N 3")))

    def test_depth_first(self):
        "Test `depth_first` enumeration."
        self.assertEqual([1], t.depth_first(t.make_df("1")))
        self.assertEqual([3, 2, 1], t.depth_first(t.make_df("1 2 3")))
        self.assertEqual([2, 1, 3], t.depth_first(t.make_df("1 2 N N 3")))
        self.assertEqual([2, 4, 1, 3], t.depth_first(t.make_df("1 2 N 4 N N 3")))

    def test_iter(self):
        "Test the level order iterator."
        self.assertEqual([1], seq(t.make_df("1")))
        self.assertEqual([2, 1, 3], seq(t.make_df("2 1 3")))
        self.assertEqual([3, 1, 2], seq(t.make_df("3 1 N N 2")))
        self.assertEqual([5, 3, 2, 4], seq(t.make_df("5 3 N 4 N N 2")))

    def test_insert(self):
        "Test `insert` function."
        self.assertEqual([1, 2], seq(t.insert(t.make_df("1"), 2)))
        self.assertEqual([2, 1, 3], seq(t.insert(t.make_df("2 1 N N 3"), 3)))
        self.assertEqual([2, 1, 3, 4], seq(t.insert(t.make_df("2 1 N N 3"), 4)))
        self.assertEqual([5, 3, 6, 2, 4], seq(t.insert(t.make_df("5 3 N 4 N N 6"), 2)))

    def test_find_ancestor(self):
        "Test `find_ancestor` function."
        self.assertEqual(2, t.find_ancestor(t.make_df("2 1"), 1, 2).data)
        self.assertEqual(2, t.find_ancestor(t.make_df("2 1 N N 3"), 3, 1).data)
        self.assertEqual(5, t.find_ancestor(t.make_df("5 3 2 N N 4 N N 6"), 4, 6).data)
        self.assertEqual(3, t.find_ancestor(t.make_df("5 3 2 N N 4 N N 6"), 3, 4).data)
        self.assertEqual(3, t.find_ancestor(t.make_df("5 3 2 N N 4 N N 6"), 2, 4).data)

    def test_largest(self):
        "Test `largest` function."
        self.assertEqual(2, t.largest(t.make_df("2 1")))
        self.assertEqual(3, t.largest(t.make_df("2 1 N N 3")))
        self.assertEqual(1, t.largest(t.make_df("2 1 N N 3"), 3))
        self.assertEqual(-1, t.largest(t.make_df("2 1 N N 3"), 4))
        self.assertEqual(6, t.largest(t.make_df("5 3 2 N N 4 N N 6"), 1))
        self.assertEqual(5, t.largest(t.make_df("5 3 2 N N 4 N N 6"), 2))
        self.assertEqual(4, t.largest(t.make_df("5 3 2 N N 4 N N 6"), 3))

    def test_successor(self):
        "Test `successor` function."
        self.assertEqual(2, t.successor(t.make_df("2 1"), 1).data)
        self.assertEqual(2, t.successor(t.make_df("2 1 N N 3"), 1).data)
        self.assertEqual(5, t.successor(t.make_df("5 3 2 N N 4 N N 6"), 4).data)
        self.assertEqual(4, t.successor(t.make_df("5 3 2 N N 4 N N 6"), 3).data)
        self.assertEqual(3, t.successor(t.make_df("5 3 2 N N 4 N N 6"), 2).data)

    def test_has_path_sum(self):
        "Test the `has_path_sum` function."
        self.assertTrue(t.has_path_sum(t.make_df("1"), 1))
        self.assertTrue(t.has_path_sum(t.make_df("1 2 3"), 6))
        self.assertTrue(t.has_path_sum(t.make_df("2 1 N N 2"), 3))
        self.assertFalse(t.has_path_sum(t.make_df("1 2 N N 3 4 5"), 6))

    def test_count_in_range(self):
        "Test `count_in_range` function."
        self.assertEqual(2, t.count_in_range(t.make_df("2 1"), 1, 2))
        self.assertEqual(2, t.count_in_range(t.make_df("2 1 N N 3"), 1, 2))
        self.assertEqual(3, t.count_in_range(t.make_df("5 3 2 N N 4 N N 6"), 2, 4))
        self.assertEqual(2, t.count_in_range(t.make_df("5 3 2 N N 4 N N 6"), 3, 4))
        self.assertEqual(2, t.count_in_range(t.make_df("5 3 2 N N 4 N N 6"), 2, 3))

    def test_median(self):
        "Test `median` function."
        self.assertEqual(1.5, t.median(t.make_df("2 1")))
        self.assertEqual(2, t.median(t.make_df("2 1 N N 3")))
        self.assertEqual(4, t.median(t.make_df("5 3 2 N N 4 N N 6")))

    def test_max_width(self):
        "Test `max_width` function."
        self.assertEqual(1, t.max_width(t.make_df("2 1")))
        self.assertEqual(2, t.max_width(t.make_df("2 1 N N 3")))
        self.assertEqual(3, t.max_width(t.make_df("5 3 2 N N 4 N N 7 6")))

    def test_to_linked_seq(self):
        "Test `to_linked_list` function."

        def it(n):
            while n:
                yield n.data
                n = n.right

        self.assertEqual([1, 2], seq(it(t.to_linked_list(t.make_df("2 1")))))
        self.assertEqual(
            [1, 3, 1, 2], seq(it(t.to_linked_list(t.make_df("2 1 1 N 3"))))
        )
        self.assertEqual(
            [2, 3, 1, 6, 7, 4, 5],
            seq(it(t.to_linked_list(t.make_df("5 3 2 N N 4 1 N 7 6")))),
        )

    def test_nodes_at_distance(self):
        "Test `nodes_at_distance`."
        self.assertEqual(
            [10, 14, 22],
            t.nodes_at_distance(t.make_df("20 8 4 N N 12 10 N N 14 N N 22"), 8, 2),
        )
        self.assertEqual(
            [1, 24],
            t.nodes_at_distance(t.make_df("20 7 4 N N 3 1 N N N 24"), 7, 2),
        )
        self.assertEqual(
            [3, 4, 20],
            t.nodes_at_distance(t.make_df("20 7 4 N N 3 1 N N N 24"), 7, 1),
        )
        self.assertEqual(
            [7],
            t.nodes_at_distance(t.make_df("20 7 4 N N 3 1 N N N 24"), 7, 0),
        )

    def test_merge_sorted(self):
        "Test `merge_sorted`."
        self.assertEqual([1], t.merge_sorted(t.make_df(""), t.make_df("1")))
        self.assertEqual([2], t.merge_sorted(t.make_df("2"), t.make_df("")))
        self.assertEqual([1, 2], t.merge_sorted(t.make_df("2"), t.make_df("1")))
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            t.merge_sorted(t.make_df("3 1 N N 5"), t.make_df("4 2 N N 6")),
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            t.merge_sorted(t.make_df("4 2 N N 6"), t.make_df("3 1 N N 5")),
        )

    def test_tree_distance(self):
        "Test `tree_distance`."
        tr = t.make("1 2 N 3 N 4 N 5 N 6 N")
        self.assertEqual(5, t.tree_distance(tr, 1))
        self.assertEqual(4, t.tree_distance(tr, 2))
        self.assertEqual(3, t.tree_distance(tr, 3))
        self.assertEqual(3, t.tree_distance(tr, 4))
        self.assertEqual(4, t.tree_distance(tr, 5))
        self.assertEqual(5, t.tree_distance(tr, 6))

        tr = t.make("1 N 2 N 3 N 4 N 5 N 6")
        self.assertEqual(5, t.tree_distance(tr, 1))
        self.assertEqual(4, t.tree_distance(tr, 2))
        self.assertEqual(3, t.tree_distance(tr, 3))
        self.assertEqual(3, t.tree_distance(tr, 4))
        self.assertEqual(4, t.tree_distance(tr, 5))
        self.assertEqual(5, t.tree_distance(tr, 6))

        tr = t.make("1 2 3 N N 4 6 N 5 N N 7 N")
        #  1___
        # /    \
        # 2  __3
        #   /   \
        #   4_  6
        #     \
        #     5
        #    /
        #    7
        self.assertEqual(4, t.tree_distance(tr, 1))
        self.assertEqual(5, t.tree_distance(tr, 2))
        self.assertEqual(3, t.tree_distance(tr, 3))
        self.assertEqual(3, t.tree_distance(tr, 4))
        self.assertEqual(4, t.tree_distance(tr, 5))
        self.assertEqual(4, t.tree_distance(tr, 6))

    def test_right_rotate(self):
        "Test `right_rotate`."
        n = None
        for x in (1, 2, 3, 4, 5):
            n = t.insert_balanced(n, x)

        self.assertEqual([2, 1, 4, 3, 5], list(n or []))
        #  2_
        # /  \
        # 1  4
        #   / \
        #   3 5

        n = n.right_rotate()
        # 1
        #  \
        #  2_
        #    \
        #    4
        #   / \
        #   3 5
        self.assertEqual([1, 2, 4, 3, 5], list(n or []))
        self.assertEqual([1, 2, 3, 4, 5], list(n.inorder()))
        self.assertEqual(4, t.height(n))

    def test_left_rotate(self):
        "Test `left_rotate`."
        n = None
        for x in (1, 2, 3, 4, 5):
            n = t.insert_balanced(n, x)

        self.assertEqual([2, 1, 4, 3, 5], list(n or []))
        #  2_
        # /  \
        # 1  4
        #   / \
        #   3 5

        n = n.left_rotate()
        #   _4
        #  /  \
        #  2  5
        # / \
        # 1 3
        self.assertEqual([4, 2, 5, 1, 3], list(n or []))
        self.assertEqual([1, 2, 3, 4, 5], list(n.inorder()))
        self.assertEqual(3, t.height(n))

    def test_insert_balanced(self):
        "Test `insert_balanced`."
        n = None
        for x in (1, 2, 3, 4, 5):
            n = t.insert_balanced(n, x)
        #  2_
        # /  \
        # 1  4
        #   / \
        #   3 5
        self.assertEqual([2, 1, 4, 3, 5], list(n or []))
        self.assertEqual([1, 2, 3, 4, 5], list(n.inorder()))
        self.assertEqual(3, t.height(n))

    def test_delete_balanced(self):
        "Test `delete_balanced`."
        n = t.make("54 44 86 43 46 78 88 N N N 50 61 83 N 89")
        #     ____54_______
        #    /             \
        #   44_         __86_
        #  /   \       /     \
        # 43  46_     78_   88_
        #        \   /   \     \
        #       50  61  83    89
        for x in (46, 86, 88, 61, 89, 78, 54, 83):
            n = n.delete_balanced(x)
        #   44_
        #  /   \
        # 43  50
        self.assertEqual("44 43 50", n.bfo_string())
        #
        n = t.make("4 2 6 1 3 5 7")
        #   _4_
        #  /   \
        #  2   6
        # / \ / \
        # 1 3 5 7
        for x in (4, 1, 3, 6):
            n = n.delete_balanced(x)
        #  5
        # / \
        # 2 7
        self.assertEqual("5 2 7", n.bfo_string())

    def test_candy_tree_equality(self):
        "Test `candy_tree_equality`."
        self.assertEqual(2, t.candy_tree_equality(t.make("3 0 0")))
        self.assertEqual(3, t.candy_tree_equality(t.make("0 3 0")))
        self.assertEqual(3, t.candy_tree_equality(t.make("0 0 3")))
        self.assertEqual(1, t.candy_tree_equality(t.make("0 1 2")))
        self.assertEqual(1, t.candy_tree_equality(t.make("2 1 0")))
        self.assertEqual(2, t.candy_tree_equality(t.make("1 2 0")))
