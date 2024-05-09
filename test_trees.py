"""Test module for the tree based puzzles."""

from __future__ import annotations

import unittest
from typing import Iterable, Iterator, Sequence

import lists as ll
import trees as t


def seq(sequence: Iterable | None) -> Sequence:
    """Return a list out of None | Iterable."""
    return list(sequence or [])


class TestTrees(unittest.TestCase):
    """Test class for the tree based puzzles."""

    def test_make(self):
        """Test tree make."""
        r = t.make("1 2 3")  # order=level
        assert r.data == 1
        assert r.left.data == 2
        assert r.right.data == 3
        assert str(r) == "1 2 3"
        assert [1, 2, 3] == seq(r)

        r = t.make("1 2 N N 3")  # order=level
        assert r.data == 1
        assert r.left.data == 2
        assert r.left.right.data == 3
        assert str(r) == "1 2 N N 3"
        assert [1, 2, 3] == seq(r)

        r = t.make("1 2 N N 3", "pre")
        assert r.data == 1
        assert r.left.data == 2
        assert r.right.data == 3
        assert str(r) == "1 2 3"
        assert [1, 2, 3] == seq(r)

    def test_inorder_postorder_tangle(self):
        """Test `inorder_postorder_tangle`."""
        r = t.inorder_postorder_tangle(
            [4, 8, 2, 5, 1, 6, 3, 7],
            [8, 4, 5, 2, 6, 7, 3, 1],
        )
        #    _1_
        #   /   \
        #  _2   3
        # /  \ / \
        # 4  5 6 7
        #  \
        #  8
        assert r.serialize("in") == "(((() 4 8) 2 5) 1 (6 3 7))"
        assert [4, 8, 2, 5, 1, 6, 3, 7] == seq(r.inorder())
        assert [8, 4, 5, 2, 6, 7, 3, 1] == seq(r.postorder())

    def test_serialize(self):
        """Test `serialize`."""
        r: t.Node = t.make("5 3 2 N N 4 N N 7 6", "pre")
        #   _5_
        #  /   \
        #  3   7
        # / \ /
        # 2 4 6
        # lvo: [5, 3, 7, 2, 4, 6]
        # pre: [5, 3, 2, 4, 7, 6]
        # ino: [2, 3, 4, 5, 6, 7]
        # pst: [2, 4, 3, 6, 7, 5]
        # lvo: 5 3 7 2 4 6
        # pre: 5 3 2 N N 4 N N 7 6
        # ino: ((2 3 4) 5 (6 7 ()))
        # pst: N N 2 N N 4 3 N N 6 N 7 5
        assert [5, 3, 7, 2, 4, 6] == seq(r)
        assert [5, 3, 2, 4, 7, 6] == seq(r.preorder())
        assert [2, 3, 4, 5, 6, 7] == seq(r.inorder())
        assert [2, 4, 3, 6, 7, 5] == seq(r.postorder())
        assert str(r) == "5 3 7 2 4 6"
        assert r.serialize("pre") == "5 3 2 N N 4 N N 7 6"
        assert r.serialize("in") == "((2 3 4) 5 (6 7))"
        assert r.serialize("post") == "N N 2 N N 4 3 N N 6 N 7 5"

        r: t.Node = t.make("1 2 4 N 3")
        #  _1
        # /  \
        # 2  4
        #  \
        #  3
        # lvo: [1, 2, 4, 3]
        # pre: [1, 2, 3, 4]
        # ino: [2, 3, 1, 4]
        # pst: [3, 2, 4, 1]
        # lvo: 1 2 4 N 3
        # pre: 1 2 N 3 N N 4
        # ino: ((() 2 3) 1 4)
        # pst: N N N 3 2 N N 4 1
        assert [1, 2, 4, 3] == seq(r)
        assert [1, 2, 3, 4] == seq(r.preorder())
        assert [2, 3, 1, 4] == seq(r.inorder())
        assert [3, 2, 4, 1] == seq(r.postorder())
        assert str(r) == "1 2 4 N 3"
        assert r.serialize("pre") == "1 2 N 3 N N 4"
        assert r.serialize("in") == "((() 2 3) 1 4)"
        assert r.serialize("post") == "N N N 3 2 N N 4 1"

        r: t.Node = t.make("1 2 4 N 3 7 N 5 N 8 9")
        #  __1___
        # /      \
        # 2_    _4
        #   \  /
        #   3  7
        #  /  / \
        #  5  8 9
        # lvo: [1, 2, 4, 3, 7, 5, 8, 9]
        # pre: [1, 2, 3, 5, 4, 7, 8, 9]
        # ino: [2, 5, 3, 1, 8, 7, 9, 4]
        # pst: [5, 3, 2, 8, 9, 7, 4, 1]
        # lvo: 1 2 4 N 3 7 N 5 N 8 9
        # pre: 1 2 N 3 5 N N N 4 7 8 N N 9
        # ino: ((() 2 (5 3)) 1 ((8 7 9) 4))
        # pst: N N N 5 N 3 2 N N 8 N N 9 7 N 4 1
        assert [1, 2, 4, 3, 7, 5, 8, 9] == seq(r)
        assert [1, 2, 3, 5, 4, 7, 8, 9] == seq(r.preorder())
        assert [2, 5, 3, 1, 8, 7, 9, 4] == seq(r.inorder())
        assert [5, 3, 2, 8, 9, 7, 4, 1] == seq(r.postorder())
        assert str(r) == "1 2 4 N 3 7 N 5 N 8 9"
        assert r.serialize("pre") == "1 2 N 3 5 N N N 4 7 8 N N 9"
        assert r.serialize("in") == "((() 2 (5 3)) 1 ((8 7 9) 4))"
        assert r.serialize("post") == "N N N 5 N 3 2 N N 8 N N 9 7 N 4 1"

    def test_from_list(self):
        """Test `from_list` constructor."""
        r: t.Node = t.from_list(ll.make([2, 3, 4, 5, 6, 7]))
        assert r.serialize("in") == "((2 3 4) 5 (6 7))"

    def test_is_bst(self):
        """Test the `is_bst` function."""
        assert t.is_bst(t.make("1"))
        assert not t.is_bst(t.make("1 2 N N 3", "pre"))
        assert t.is_bst(t.make("2 1 N N 3", "pre"))
        assert not t.is_bst(t.make("2 3 N N 1", "pre"))

    def test_left_view(self):
        """Test the `left_view` function."""
        assert [1] == t.left_view(t.make("1"))
        assert [1, 2, 3] == t.left_view(t.make("1 2 3", "pre"))
        assert [1, 2] == t.left_view(t.make("1 2 N N 3", "pre"))
        assert [1, 2, 4] == t.left_view(t.make("1 2 N N 3 4", "pre"))

    def test_balanced(self):
        """Test the `balanced` function."""
        assert t.balanced(t.make("1"))
        assert not t.balanced(t.make("1 2 N N 3"))
        assert t.balanced(t.make("1 2 N N 3", "pre"))
        assert not t.balanced(t.make("1 2 N N 3 4 5", "pre"))

    def test_identical(self):
        """Test the `identical` function."""
        assert t.identical(t.make("1"), t.make("1"))
        assert not t.identical(t.make("1"), t.make("1 2 3"))
        assert t.identical(t.make("1 2 N N 3", "pre"), t.make("1 2 N N 3", "pre"))
        assert not t.identical(
            t.make("1 2 N N 3", "pre"),
            t.make("1 2 N N 3 4 5", "pre"),
        )

    def test_symmetric(self):
        """Test the `symmetric` function."""
        assert t.symmetric(t.make("1"))
        assert not t.symmetric(t.make("1 2 3"))
        assert t.symmetric(t.make("1 2 N N 2", "pre"))
        assert not t.symmetric(t.make("1 2 N N 2 2 2", "pre"))

    def test_flat(self):
        """Test the `flat` function."""
        assert t.flat(t.make("1"))
        assert t.flat(t.make("1 2 3"))
        assert t.flat(t.make("2 1 N N 2", "pre"))
        assert not t.flat(t.make("1 2 N N 3 4 5", "pre"))

    def test_default_level_order_iterator(self):
        """Test __iter__ enumeration."""
        assert [1] == seq(t.make("1"))
        assert [1, 2, 3] == seq(t.make("1 2 3"))
        assert [1, 2, 3] == seq(t.make("1 2 N N 3", "pre"))
        assert [1, 2, 3, 4] == seq(t.make("1 2 N 4 N N 3", "pre"))

    def test_depth_first_inorder_iterator(self):
        """Test `inorder` enumeration."""
        assert [1] == seq(t.make("1").inorder())
        assert [2, 1, 3] == seq(t.make("1 2 3").inorder())
        assert [2, 3, 1] == seq(t.make("1 2 N N 3").inorder())
        assert [2, 1, 3] == seq(t.make("1 2 N N 3", "pre").inorder())
        assert [2, 4, 1, 3] == seq(t.make("1 2 N 4 N N 3", "pre").inorder())

    def test_iter(self):
        """Test the level order iterator."""
        assert [1] == seq(t.make("1"))
        assert [2, 1, 3] == seq(t.make("2 1 3"))
        assert [3, 1, 2] == seq(t.make("3 1 N N 2", "pre"))
        assert [5, 3, 2, 4] == seq(t.make("5 3 N 4 N N 2", "pre"))

    def test_insert(self):
        """Test `insert` function."""
        assert [1, 2] == seq(t.insert(t.make("1"), 2))
        assert [2, 1, 3] == seq(t.insert(t.make("2 1 N N 3", "pre"), 3))
        assert [2, 1, 3, 4] == seq(t.insert(t.make("2 1 N N 3", "pre"), 4))
        assert [5, 3, 6, 2, 4] == seq(t.insert(t.make("5 3 N 4 N N 6", "pre"), 2))

    def test_find_bst_ancestor(self):
        """Test `find_bst_ancestor` function."""
        assert t.find_bst_ancestor(t.make("2 1"), 1, 2).data == 2
        assert t.find_bst_ancestor(t.make("2 1 N N 3", "pre"), 3, 1).data == 2
        assert t.find_bst_ancestor(t.make("5 3 2 N N 4 N N 6", "pre"), 4, 6).data == 5
        assert t.find_bst_ancestor(t.make("5 3 2 N N 4 N N 6", "pre"), 3, 4).data == 3
        assert t.find_bst_ancestor(t.make("5 3 2 N N 4 N N 6", "pre"), 2, 4).data == 3

    def test_lowest_common_ancestor(self):
        """Test `lowest_common_ancestor` function."""
        assert t.lowest_common_ancestor(t.make("2 1"), 1, 2).data == 2
        assert t.lowest_common_ancestor(t.make("1 2 3"), 2, 3).data == 1
        assert t.lowest_common_ancestor(t.make("1 2 3"), 1, 3).data == 1
        assert t.lowest_common_ancestor(t.make("1 2 3"), 1, 2).data == 1
        assert t.lowest_common_ancestor(t.make("1 2 3 4 5 6 7"), 5, 6).data == 1
        assert t.lowest_common_ancestor(t.make("1 2 3 4 5 6 7"), 4, 5).data == 2
        assert t.lowest_common_ancestor(t.make("1 2 3 4 5 6 7"), 4, 7).data == 1

    def test_largest(self):
        """Test `largest` function."""
        assert t.largest(t.make("2 1")) == 2
        assert t.largest(t.make("2 1 N N 3", "pre")) == 3
        assert t.largest(t.make("2 1 N N 3", "pre"), 3) == 1
        assert t.largest(t.make("2 1 N N 3", "pre"), 4) == -1
        assert t.largest(t.make("5 3 2 N N 4 N N 6", "pre"), 1) == 6
        assert t.largest(t.make("5 3 2 N N 4 N N 6", "pre"), 2) == 5
        assert t.largest(t.make("5 3 2 N N 4 N N 6", "pre"), 3) == 4

    def test_successor(self):
        """Test `successor` function."""
        assert t.successor(t.make("2 1"), 1).data == 2
        assert t.successor(t.make("2 1 N N 3", "pre"), 1).data == 2
        assert t.successor(t.make("5 3 2 N N 4 N N 6", "pre"), 4).data == 5
        assert t.successor(t.make("5 3 2 N N 4 N N 6", "pre"), 3).data == 4
        assert t.successor(t.make("5 3 2 N N 4 N N 6", "pre"), 2).data == 3

    def test_has_path_sum(self):
        """Test the `has_path_sum` function."""
        assert t.has_path_sum(t.make("1"), 1)
        assert t.has_path_sum(t.make("1 2 3", "pre"), 6)
        assert t.has_path_sum(t.make("2 1 N N 2", "pre"), 3)
        assert not t.has_path_sum(t.make("1 2 N N 3 4 5", "pre"), 6)

    def test_count_in_range(self):
        """Test `count_in_range` function."""
        assert t.count_in_range(t.make("2 1", "pre"), 1, 2) == 2
        assert t.count_in_range(t.make("2 1 N N 3", "pre"), 1, 2) == 2
        assert t.count_in_range(t.make("5 3 2 N N 4 N N 6", "pre"), 2, 4) == 3
        assert t.count_in_range(t.make("5 3 2 N N 4 N N 6", "pre"), 3, 4) == 2
        assert t.count_in_range(t.make("5 3 2 N N 4 N N 6", "pre"), 2, 3) == 2

    def test_median(self):
        """Test `median` function."""
        assert t.median(t.make("2 1")) == 1.5
        assert t.median(t.make("2 1 N N 3", "pre")) == 2
        assert t.median(t.make("5 3 2 N N 4 N N 6", "pre")) == 4

    def test_max_width(self):
        """Test `max_width` function."""
        assert t.max_width(t.make("2 1")) == 1
        assert t.max_width(t.make("1 2 3")) == 2
        assert t.max_width(t.make("5 3 2 N N 4 N N 7 6", "pre")) == 3

    def test_to_linked_seq(self):
        """Test `to_linked_list` function."""

        def it(n: t.Node) -> Iterator[int]:
            while n:
                yield n.data
                n = n.right

        assert [1, 2] == seq(it(t.to_linked_list(t.make("2 1"))))
        assert [1, 3, 1, 2] == seq(it(t.to_linked_list(t.make("2 1 1 N 3", "pre"))))
        assert [2, 3, 1, 6, 7, 4, 5] == seq(
            it(t.to_linked_list(t.make("5 3 2 N N 4 1 N 7 6", "pre"))),
        )

    def test_nodes_at_distance(self):
        """Test `nodes_at_distance`."""
        assert [10, 14, 22] == t.nodes_at_distance(
            t.make("20 8 4 N N 12 10 N N 14 N N 22", "pre"),
            8,
            2,
        )
        assert [1, 24] == t.nodes_at_distance(
            t.make("20 7 4 N N 3 1 N N N 24", "pre"),
            7,
            2,
        )
        assert [3, 4, 20] == t.nodes_at_distance(
            t.make("20 7 4 N N 3 1 N N N 24", "pre"),
            7,
            1,
        )
        assert [7] == t.nodes_at_distance(
            t.make("20 7 4 N N 3 1 N N N 24", "pre"),
            7,
            0,
        )

    def test_merge_sorted(self):
        """Test `merge_sorted`."""
        assert [1] == t.merge_sorted(t.make(""), t.make("1"))
        assert [2] == t.merge_sorted(t.make("2"), t.make(""))
        assert [1, 2] == t.merge_sorted(t.make("2"), t.make("1"))
        assert [1, 2, 3, 4, 5, 6] == t.merge_sorted(
            t.make("3 1 N N 5", "pre"),
            t.make("4 2 N N 6", "pre"),
        )
        assert [1, 2, 3, 4, 5, 6] == t.merge_sorted(
            t.make("4 2 N N 6", "pre"),
            t.make("3 1 N N 5", "pre"),
        )

    def test_tree_distance(self):
        """Test `tree_distance`."""
        tr = t.make("1 2 N 3 N 4 N 5 N 6 N")
        assert t.tree_distance(tr, 1) == 5
        assert t.tree_distance(tr, 2) == 4
        assert t.tree_distance(tr, 3) == 3
        assert t.tree_distance(tr, 4) == 3
        assert t.tree_distance(tr, 5) == 4
        assert t.tree_distance(tr, 6) == 5

        tr = t.make("1 N 2 N 3 N 4 N 5 N 6")
        assert t.tree_distance(tr, 1) == 5
        assert t.tree_distance(tr, 2) == 4
        assert t.tree_distance(tr, 3) == 3
        assert t.tree_distance(tr, 4) == 3
        assert t.tree_distance(tr, 5) == 4
        assert t.tree_distance(tr, 6) == 5

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
        assert t.tree_distance(tr, 1) == 4
        assert t.tree_distance(tr, 2) == 5
        assert t.tree_distance(tr, 3) == 3
        assert t.tree_distance(tr, 4) == 3
        assert t.tree_distance(tr, 5) == 4
        assert t.tree_distance(tr, 6) == 4

    def test_right_rotate(self):
        """Test `right_rotate`."""
        n = None
        for x in (1, 2, 3, 4, 5):
            n = t.insert_balanced(n, x)

        assert [2, 1, 4, 3, 5] == list(n or [])
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
        assert [1, 2, 4, 3, 5] == list(n or [])
        assert [1, 2, 3, 4, 5] == list(n.inorder())
        assert t.height(n) == 4

    def test_left_rotate(self):
        """Test `left_rotate`."""
        n = None
        for x in (1, 2, 3, 4, 5):
            n = t.insert_balanced(n, x)

        assert [2, 1, 4, 3, 5] == list(n or [])
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
        assert [4, 2, 5, 1, 3] == list(n or [])
        assert [1, 2, 3, 4, 5] == list(n.inorder())
        assert t.height(n) == 3

    def test_insert_balanced(self):
        """Test `insert_balanced`."""
        n = None
        for x in (1, 2, 3, 4, 5):
            n = t.insert_balanced(n, x)
        #  2_
        # /  \
        # 1  4
        #   / \
        #   3 5
        assert [2, 1, 4, 3, 5] == list(n or [])
        assert [1, 2, 3, 4, 5] == list(n.inorder())
        assert t.height(n) == 3

    def test_delete_balanced(self):
        """Test `delete_balanced`."""
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
        assert str(n) == "44 43 50"
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
        assert str(n) == "5 2 7"

    def test_candy_tree_equality(self):
        """Test `candy_tree_equality`."""
        assert t.candy_tree_equality(t.make("3 0 0")) == 2
        assert t.candy_tree_equality(t.make("0 3 0")) == 3
        assert t.candy_tree_equality(t.make("0 0 3")) == 3
        assert t.candy_tree_equality(t.make("0 1 2")) == 1
        assert t.candy_tree_equality(t.make("2 1 0")) == 1
        assert t.candy_tree_equality(t.make("1 2 0")) == 2

    def test_min_bst_with_a_sum(self):
        """Test `min_bst_with_a_sum`."""
        r = t.make("1")
        assert t.min_bst_with_a_sum(r, 1) == 1
        r = t.make("1 2 3")
        assert t.min_bst_with_a_sum(r, 2) == 1
        assert t.min_bst_with_a_sum(r, 3) == 1
        assert t.min_bst_with_a_sum(r, 6) == -1
        r = t.make("2 1 3")
        assert t.min_bst_with_a_sum(r, 1) == 1
        assert t.min_bst_with_a_sum(r, 2) == -1
        assert t.min_bst_with_a_sum(r, 6) == 3
        r = t.make("1 N 3 2 4")
        assert t.min_bst_with_a_sum(r, 10) == 4
        r = t.make("1 N 3 1 5")
        assert t.min_bst_with_a_sum(r, 10) == -1
        r = t.make("27 24 N 17 26 10 N N N N 12 10 14")
        assert t.min_bst_with_a_sum(r, 113) == -1
        r = t.make(
            "5146 8127 4333 7177 370  3598 4005 2737 8147 918  2423 "
            "4418 3658 3965 3609 4506 7905 3531 5786 7069 5986 4125 "
            "3109 5378 3898 6654 2270 2614 8579 7243 8788",
        )
        assert t.min_bst_with_a_sum(r, 4125) == 1

    def test_number_of_turns(self):
        """Test `number_of_turns`."""
        assert t.number_of_turns(t.make("1 2 3"), 2, 3) == 1
        assert t.number_of_turns(t.make("1 2 3"), 3, 2) == 1
        assert t.number_of_turns(t.make("1 2 3"), 1, 1) == 0
        assert t.number_of_turns(t.make("1 2 3"), 2, 2) == 0
        assert t.number_of_turns(t.make("1 2 3"), 3, 3) == 0
        assert t.number_of_turns(t.make("1 2 3"), 1, 3) == 0
        assert t.number_of_turns(t.make("1 2 3"), 2, 1) == 0
        assert t.number_of_turns(t.make("1 2 N N 4"), 1, 4) == 1
        assert t.number_of_turns(t.make("1 2 3 N 4 N N 5"), 1, 5) == 2
        assert t.number_of_turns(t.make("1 2 3 4 5 6 7"), 5, 6) == 3
        assert t.number_of_turns(t.make("1 2 3 4 5 6 7 8 N N N 9 10"), 5, 10) == 4
