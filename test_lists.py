"""Test module for the linked lists puzzles."""

from __future__ import annotations

import unittest
from typing import Iterable, Sequence

import lists as ll


def seq(sequence: Iterable | None) -> Sequence:
    """Return a list out of None | Iterable."""
    return list(sequence or [])


class TestLinkedLists(unittest.TestCase):
    """Test class for the linked lists puzzles."""

    def test_make_linked(self):
        """Test `make_linked`."""
        assert ll.make([]) is None

        n = ll.make([0, 1, 2])
        assert n.data == 0
        n = n.next
        assert n.data == 1
        n = n.next
        assert n.data == 2
        assert n.next is None

    def test_make_linked_loop(self):
        """Test `make_linked`."""
        assert ll.make([], 0) is None

        n = ll.make([0, 1, 2], 0)
        assert n.data == 0
        n = n.next
        assert n.data == 1
        n = n.next
        assert n.data == 2
        n = n.next
        assert n.data == 0

        n = ll.make([0, 1, 2], 2)
        assert n.data == 0
        n = n.next
        assert n.data == 1
        n = n.next
        assert n.data == 2
        n = n.next
        assert n.data == 2

    def subtest_slicing(self, arr: list, linked_list: ll.Node):  # noqa: PLR0915
        """Assert that `arr` and `lst` slice the same way."""
        lst = linked_list or []
        assert arr == lst[:]
        assert arr[0:] == lst[0:]
        assert arr[1:] == lst[1:]
        assert arr[2:] == lst[2:]
        assert arr[3:] == lst[3:]
        assert arr[:0] == lst[:0]
        assert arr[:1] == lst[:1]
        assert arr[:2] == lst[:2]
        assert arr[:3] == lst[:3]

        assert arr[-1:] == lst[-1:]
        assert arr[-2:] == lst[-2:]
        assert arr[-3:] == lst[-3:]
        assert arr[:-0] == lst[:-0]
        assert arr[:-1] == lst[:-1]
        assert arr[:-2] == lst[:-2]
        assert arr[:-3] == lst[:-3]

        assert arr[::-1] == lst[::-1]
        assert arr[0::-1] == lst[0::-1]
        assert arr[1::-1] == lst[1::-1]
        assert arr[2::-1] == lst[2::-1]
        assert arr[3::-1] == lst[3::-1]
        assert arr[:0:-1] == lst[:0:-1]
        assert arr[:1:-1] == lst[:1:-1]
        assert arr[:2:-1] == lst[:2:-1]
        assert arr[:3:-1] == lst[:3:-1]

        assert arr[-1::-1] == lst[-1::-1]
        assert arr[-2::-1] == lst[-2::-1]
        assert arr[-3::-1] == lst[-3::-1]
        assert arr[:-1:-1] == lst[:-1:-1]
        assert arr[:-2:-1] == lst[:-2:-1]
        assert arr[:-3:-1] == lst[:-3:-1]

        assert arr[::-2] == lst[::-2]
        assert arr[0::-2] == lst[0::-2]
        assert arr[1::-2] == lst[1::-2]
        assert arr[2::-2] == lst[2::-2]
        assert arr[3::-2] == lst[3::-2]
        assert arr[:0:-2] == lst[:0:-2]
        assert arr[:1:-2] == lst[:1:-2]
        assert arr[:2:-2] == lst[:2:-2]
        assert arr[:3:-2] == lst[:3:-2]

        assert arr[-1::-2] == lst[-1::-2]
        assert arr[-2::-2] == lst[-2::-2]
        assert arr[-3::-2] == lst[-3::-2]
        assert arr[:-1:-2] == lst[:-1:-2]
        assert arr[:-2:-2] == lst[:-2:-2]
        assert arr[:-3:-2] == lst[:-3:-2]

        assert arr[::-3] == lst[::-3]
        assert arr[0::-3] == lst[0::-3]
        assert arr[1::-3] == lst[1::-3]
        assert arr[2::-3] == lst[2::-3]
        assert arr[3::-3] == lst[3::-3]
        assert arr[:0:-3] == lst[:0:-3]
        assert arr[:1:-3] == lst[:1:-3]
        assert arr[:2:-3] == lst[:2:-3]
        assert arr[:3:-3] == lst[:3:-3]

        assert arr[-1::-3] == lst[-1::-3]
        assert arr[-2::-3] == lst[-2::-3]
        assert arr[-3::-3] == lst[-3::-3]
        assert arr[:-1:-3] == lst[:-1:-3]
        assert arr[:-2:-3] == lst[:-2:-3]
        assert arr[:-3:-3] == lst[:-3:-3]

        assert arr[0:] == lst[0:]
        assert arr[1:] == lst[1:]
        assert arr[7:] == lst[7:]
        assert arr[70:] == lst[70:]
        assert arr[:0] == lst[:0]
        assert arr[:1] == lst[:1]
        assert arr[:3] == lst[:3]
        assert arr[:30] == lst[:30]

        assert arr[::2] == lst[::2]
        assert arr[0::2] == lst[0::2]
        assert arr[1::2] == lst[1::2]
        assert arr[7::2] == lst[7::2]
        assert arr[70::2] == lst[70::2]
        assert arr[:0:2] == lst[:0:2]
        assert arr[:1:2] == lst[:1:2]
        assert arr[:3:2] == lst[:3:2]
        assert arr[:30:2] == lst[:30:2]

        assert arr[::3] == lst[::3]
        assert arr[0::3] == lst[0::3]
        assert arr[1::3] == lst[1::3]
        assert arr[7::3] == lst[7::3]
        assert arr[70::3] == lst[70::3]
        assert arr[:0:3] == lst[:0:3]
        assert arr[:1:3] == lst[:1:3]
        assert arr[:3:3] == lst[:3:3]
        assert arr[:30:3] == lst[:30:3]

        assert arr[::11] == lst[::11]
        assert arr[0::11] == lst[0::11]
        assert arr[1::11] == lst[1::11]
        assert arr[7::11] == lst[7::11]
        assert arr[70::11] == lst[70::11]
        assert arr[:0:11] == lst[:0:11]
        assert arr[:1:11] == lst[:1:11]
        assert arr[:3:11] == lst[:3:11]
        assert arr[:30:11] == lst[:30:11]

        assert arr[::-1] == lst[::-1]
        assert arr[0::-1] == lst[0::-1]
        assert arr[1::-1] == lst[1::-1]
        assert arr[7::-1] == lst[7::-1]
        assert arr[70::-1] == lst[70::-1]
        assert arr[:0:-1] == lst[:0:-1]
        assert arr[:1:-1] == lst[:1:-1]
        assert arr[:3:-1] == lst[:3:-1]
        assert arr[:30:-1] == lst[:30:-1]
        assert arr[30:1:-1] == lst[30:1:-1]
        assert arr[7:1:-1] == lst[7:1:-1]
        assert arr[6:1:-1] == lst[6:1:-1]
        assert arr[1:1:-1] == lst[1:1:-1]

        assert arr[::-2] == lst[::-2]
        assert arr[0::-2] == lst[0::-2]
        assert arr[1::-2] == lst[1::-2]
        assert arr[7::-2] == lst[7::-2]
        assert arr[70::-2] == lst[70::-2]
        assert arr[:0:-2] == lst[:0:-2]
        assert arr[:1:-2] == lst[:1:-2]
        assert arr[:3:-2] == lst[:3:-2]
        assert arr[:30:-2] == lst[:30:-2]
        assert arr[30:1:-2] == lst[30:1:-2]
        assert arr[7:1:-2] == lst[7:1:-2]
        assert arr[6:1:-2] == lst[6:1:-2]
        assert arr[1:1:-2] == lst[1:1:-2]

        assert arr[::-3] == lst[::-3]
        assert arr[0::-3] == lst[0::-3]
        assert arr[1::-3] == lst[1::-3]
        assert arr[7::-3] == lst[7::-3]
        assert arr[70::-3] == lst[70::-3]
        assert arr[:0:-3] == lst[:0:-3]
        assert arr[:1:-3] == lst[:1:-3]
        assert arr[:3:-3] == lst[:3:-3]
        assert arr[:30:-3] == lst[:30:-3]
        assert arr[30:1:-3] == lst[30:1:-3]
        assert arr[7:1:-3] == lst[7:1:-3]
        assert arr[6:1:-3] == lst[6:1:-3]
        assert arr[1:1:-3] == lst[1:1:-3]

    def test_slicing(self):
        """Test slicing."""
        arr = [0]
        lst = ll.make(arr)
        self.subtest_slicing(arr, lst)
        arr = [0, 1]
        lst = ll.make(arr)
        self.subtest_slicing(arr, lst)
        arr = [0, 1, 2]
        lst = ll.make(arr)
        self.subtest_slicing(arr, lst)
        arr = [0, 1, 2, 3]
        lst = ll.make(arr)
        self.subtest_slicing(arr, lst)

        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        lst = ll.make(arr)
        self.subtest_slicing(arr, lst)

    def test_middle(self):
        """Test `middle` node function."""
        assert ll.middle(ll.make([])) is None

        assert ll.middle(ll.make([1])).data == 1
        assert ll.middle(ll.make([1, 2])).data == 2
        assert ll.middle(ll.make([1, 2, 3])).data == 2
        assert ll.middle(ll.make([1, 2, 3, 4])).data == 3

    def test_delete_middle(self):
        """Test `delete_middle` node function."""
        assert ll.delete_middle(ll.make([])) is None
        assert ll.delete_middle(ll.make([1])) is None

        assert [1] == seq(ll.delete_middle(ll.make([1, 2])))
        assert [1, 3] == seq(ll.delete_middle(ll.make([1, 2, 3])))
        assert [1, 2, 4] == seq(ll.delete_middle(ll.make([1, 2, 3, 4])))

    def test_nth(self):
        """Test `nth` function."""
        l = ll.make([1, 2, 3, 4])
        assert ll.nth(l, 0).data == 1
        assert ll.nth(l, 3).data == 4
        assert ll.nth(l, -1).data == 4
        assert ll.nth(l, -4).data == 1
        assert ll.nth(l, 4) is None
        assert ll.nth(l, -5) is None

        e = ll.make([])
        assert ll.nth(e, 0) is None
        assert ll.nth(e, 1000) is None
        assert ll.nth(e, -1000) is None

    def test_insert_sorted(self):
        """Test `insert_sorted`."""
        assert [1] == seq(ll.insert_sorted(ll.make([]), 1))
        assert [1, 2] == seq(ll.insert_sorted(ll.make([1]), 2))
        assert [1, 2] == seq(ll.insert_sorted(ll.make([2]), 1))
        assert [1, 2, 3] == seq(ll.insert_sorted(ll.make([1, 3]), 2))

    def test_reverse(self):
        """Test `reverse`."""
        assert ll.reverse(ll.make([])) is None

        assert [1] == seq(ll.reverse(ll.make([1])))
        assert [2, 1] == seq(ll.reverse(ll.make([1, 2])))
        assert [3, 2, 1] == seq(ll.reverse(ll.make([1, 2, 3])))

    def test_dedup(self):
        """Test `dedup` function."""
        assert ll.dedup(ll.make([])) is None

        assert [1] == seq(ll.dedup(ll.make([1])))
        assert [1, 2, 3] == seq(ll.dedup(ll.make([1, 2, 3])))
        assert [3, 2] == seq(ll.dedup(ll.make([3, 2, 3])))
        assert [1, 3] == seq(ll.dedup(ll.make([1, 3, 3])))
        assert [1, 3] == seq(ll.dedup(ll.make([1, 1, 3])))

    def test_loop_length(self):
        """Test the `loop_length` function."""
        assert ll.loop_length(ll.make([])) == 0
        assert ll.loop_length(ll.make([1])) == 0
        assert ll.loop_length(ll.make([1], 0)) == 1
        assert ll.loop_length(ll.make([1, 2, 3])) == 0
        assert ll.loop_length(ll.make([1, 2, 3], 2)) == 1
        assert ll.loop_length(ll.make([1, 2, 3], 1)) == 2
        assert ll.loop_length(ll.make([1, 2, 3], 0)) == 3

    def test_swap_pairs(self):
        """Test `swap_pairs` function."""
        assert ll.swap_pairs(ll.make([])) is None

        assert [1] == seq(ll.swap_pairs(ll.make([1])))
        assert [2, 1] == seq(ll.swap_pairs(ll.make([1, 2])))
        assert [2, 1, 3] == seq(ll.swap_pairs(ll.make([1, 2, 3])))
        assert [2, 1, 4, 3] == seq(ll.swap_pairs(ll.make([1, 2, 3, 4])))

    def test_subtract_lists(self):
        """Test `subtract_lists` function."""
        assert [8, 8] == seq(
            ll.subtract_lists(
                ll.make(list(map(int, "100"))),
                ll.make(list(map(int, "12"))),
            ),
        )
        l = ll.subtract_lists(
            ll.make(list(map(int, "020055383525634518999521060086463321841"))),
            ll.make(list(map(int, "10835173613544430215114275094755963004"))),
        )
        assert "".join(map(str, l or [])) == "9220209912090088784406784991707358837"
