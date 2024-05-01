"""Test module for the linked lists puzzles."""

import unittest
from typing import Iterable, Optional, Sequence

import lists as ll


def seq(sequence: Optional[Iterable]) -> Sequence:
    "Return a list out of None | Iterable."
    return list(sequence or [])


class TestLinkedLists(unittest.TestCase):
    """Test class for the linked lists puzzles."""

    def test_make_linked(self):
        "Test `make_linked`."
        self.assertIsNone(ll.make([]))

        n = ll.make([0, 1, 2])
        self.assertEqual(0, n.data)
        n = n.next
        self.assertEqual(1, n.data)
        n = n.next
        self.assertEqual(2, n.data)
        self.assertIsNone(n.next)

    def test_make_linked_loop(self):
        "Test `make_linked`."
        self.assertIsNone(ll.make([], 0))

        n = ll.make([0, 1, 2], 0)
        self.assertEqual(0, n.data)
        n = n.next
        self.assertEqual(1, n.data)
        n = n.next
        self.assertEqual(2, n.data)
        n = n.next
        self.assertEqual(0, n.data)

        n = ll.make([0, 1, 2], 2)
        self.assertEqual(0, n.data)
        n = n.next
        self.assertEqual(1, n.data)
        n = n.next
        self.assertEqual(2, n.data)
        n = n.next
        self.assertEqual(2, n.data)

    def subtest_slicing(self, arr, lst):
        "Helper for the slicing test."
        self.assertEqual(arr, lst[:])
        self.assertEqual(arr[0:], lst[0:])
        self.assertEqual(arr[1:], lst[1:])
        self.assertEqual(arr[2:], lst[2:])
        self.assertEqual(arr[3:], lst[3:])
        self.assertEqual(arr[:0:], lst[:0:])
        self.assertEqual(arr[:1:], lst[:1:])
        self.assertEqual(arr[:2:], lst[:2:])
        self.assertEqual(arr[:3:], lst[:3:])

        self.assertEqual(arr[-1:], lst[-1:])
        self.assertEqual(arr[-2:], lst[-2:])
        self.assertEqual(arr[-3:], lst[-3:])
        self.assertEqual(arr[:-0:], lst[:-0:])
        self.assertEqual(arr[:-1:], lst[:-1:])
        self.assertEqual(arr[:-2:], lst[:-2:])
        self.assertEqual(arr[:-3:], lst[:-3:])

        self.assertEqual(arr[::-1], lst[::-1])
        self.assertEqual(arr[0::-1], lst[0::-1])
        self.assertEqual(arr[1::-1], lst[1::-1])
        self.assertEqual(arr[2::-1], lst[2::-1])
        self.assertEqual(arr[3::-1], lst[3::-1])
        self.assertEqual(arr[:0:-1], lst[:0:-1])
        self.assertEqual(arr[:1:-1], lst[:1:-1])
        self.assertEqual(arr[:2:-1], lst[:2:-1])
        self.assertEqual(arr[:3:-1], lst[:3:-1])

        self.assertEqual(arr[-1::-1], lst[-1::-1])
        self.assertEqual(arr[-2::-1], lst[-2::-1])
        self.assertEqual(arr[-3::-1], lst[-3::-1])
        self.assertEqual(arr[:-1:-1], lst[:-1:-1])
        self.assertEqual(arr[:-2:-1], lst[:-2:-1])
        self.assertEqual(arr[:-3:-1], lst[:-3:-1])

        self.assertEqual(arr[::-2], lst[::-2])
        self.assertEqual(arr[0::-2], lst[0::-2])
        self.assertEqual(arr[1::-2], lst[1::-2])
        self.assertEqual(arr[2::-2], lst[2::-2])
        self.assertEqual(arr[3::-2], lst[3::-2])
        self.assertEqual(arr[:0:-2], lst[:0:-2])
        self.assertEqual(arr[:1:-2], lst[:1:-2])
        self.assertEqual(arr[:2:-2], lst[:2:-2])
        self.assertEqual(arr[:3:-2], lst[:3:-2])

        self.assertEqual(arr[-1::-2], lst[-1::-2])
        self.assertEqual(arr[-2::-2], lst[-2::-2])
        self.assertEqual(arr[-3::-2], lst[-3::-2])
        self.assertEqual(arr[:-1:-2], lst[:-1:-2])
        self.assertEqual(arr[:-2:-2], lst[:-2:-2])
        self.assertEqual(arr[:-3:-2], lst[:-3:-2])

        self.assertEqual(arr[::-3], lst[::-3])
        self.assertEqual(arr[0::-3], lst[0::-3])
        self.assertEqual(arr[1::-3], lst[1::-3])
        self.assertEqual(arr[2::-3], lst[2::-3])
        self.assertEqual(arr[3::-3], lst[3::-3])
        self.assertEqual(arr[:0:-3], lst[:0:-3])
        self.assertEqual(arr[:1:-3], lst[:1:-3])
        self.assertEqual(arr[:2:-3], lst[:2:-3])
        self.assertEqual(arr[:3:-3], lst[:3:-3])

        self.assertEqual(arr[-1::-3], lst[-1::-3])
        self.assertEqual(arr[-2::-3], lst[-2::-3])
        self.assertEqual(arr[-3::-3], lst[-3::-3])
        self.assertEqual(arr[:-1:-3], lst[:-1:-3])
        self.assertEqual(arr[:-2:-3], lst[:-2:-3])
        self.assertEqual(arr[:-3:-3], lst[:-3:-3])

        self.assertEqual(arr[0:], lst[0:])
        self.assertEqual(arr[1:], lst[1:])
        self.assertEqual(arr[7:], lst[7:])
        self.assertEqual(arr[70:], lst[70:])
        self.assertEqual(arr[:0], lst[:0])
        self.assertEqual(arr[:1], lst[:1])
        self.assertEqual(arr[:3], lst[:3])
        self.assertEqual(arr[:30], lst[:30])

        self.assertEqual(arr[::2], lst[::2])
        self.assertEqual(arr[0::2], lst[0::2])
        self.assertEqual(arr[1::2], lst[1::2])
        self.assertEqual(arr[7::2], lst[7::2])
        self.assertEqual(arr[70::2], lst[70::2])
        self.assertEqual(arr[:0:2], lst[:0:2])
        self.assertEqual(arr[:1:2], lst[:1:2])
        self.assertEqual(arr[:3:2], lst[:3:2])
        self.assertEqual(arr[:30:2], lst[:30:2])

        self.assertEqual(arr[::3], lst[::3])
        self.assertEqual(arr[0::3], lst[0::3])
        self.assertEqual(arr[1::3], lst[1::3])
        self.assertEqual(arr[7::3], lst[7::3])
        self.assertEqual(arr[70::3], lst[70::3])
        self.assertEqual(arr[:0:3], lst[:0:3])
        self.assertEqual(arr[:1:3], lst[:1:3])
        self.assertEqual(arr[:3:3], lst[:3:3])
        self.assertEqual(arr[:30:3], lst[:30:3])

        self.assertEqual(arr[::11], lst[::11])
        self.assertEqual(arr[0::11], lst[0::11])
        self.assertEqual(arr[1::11], lst[1::11])
        self.assertEqual(arr[7::11], lst[7::11])
        self.assertEqual(arr[70::11], lst[70::11])
        self.assertEqual(arr[:0:11], lst[:0:11])
        self.assertEqual(arr[:1:11], lst[:1:11])
        self.assertEqual(arr[:3:11], lst[:3:11])
        self.assertEqual(arr[:30:11], lst[:30:11])

        self.assertEqual(arr[::-1], lst[::-1])
        self.assertEqual(arr[0::-1], lst[0::-1])
        self.assertEqual(arr[1::-1], lst[1::-1])
        self.assertEqual(arr[7::-1], lst[7::-1])
        self.assertEqual(arr[70::-1], lst[70::-1])
        self.assertEqual(arr[:0:-1], lst[:0:-1])
        self.assertEqual(arr[:1:-1], lst[:1:-1])
        self.assertEqual(arr[:3:-1], lst[:3:-1])
        self.assertEqual(arr[:30:-1], lst[:30:-1])
        self.assertEqual(arr[30:1:-1], lst[30:1:-1])
        self.assertEqual(arr[7:1:-1], lst[7:1:-1])
        self.assertEqual(arr[6:1:-1], lst[6:1:-1])
        self.assertEqual(arr[1:1:-1], lst[1:1:-1])

        self.assertEqual(arr[::-2], lst[::-2])
        self.assertEqual(arr[0::-2], lst[0::-2])
        self.assertEqual(arr[1::-2], lst[1::-2])
        self.assertEqual(arr[7::-2], lst[7::-2])
        self.assertEqual(arr[70::-2], lst[70::-2])
        self.assertEqual(arr[:0:-2], lst[:0:-2])
        self.assertEqual(arr[:1:-2], lst[:1:-2])
        self.assertEqual(arr[:3:-2], lst[:3:-2])
        self.assertEqual(arr[:30:-2], lst[:30:-2])
        self.assertEqual(arr[30:1:-2], lst[30:1:-2])
        self.assertEqual(arr[7:1:-2], lst[7:1:-2])
        self.assertEqual(arr[6:1:-2], lst[6:1:-2])
        self.assertEqual(arr[1:1:-2], lst[1:1:-2])

        self.assertEqual(arr[::-3], lst[::-3])
        self.assertEqual(arr[0::-3], lst[0::-3])
        self.assertEqual(arr[1::-3], lst[1::-3])
        self.assertEqual(arr[7::-3], lst[7::-3])
        self.assertEqual(arr[70::-3], lst[70::-3])
        self.assertEqual(arr[:0:-3], lst[:0:-3])
        self.assertEqual(arr[:1:-3], lst[:1:-3])
        self.assertEqual(arr[:3:-3], lst[:3:-3])
        self.assertEqual(arr[:30:-3], lst[:30:-3])
        self.assertEqual(arr[30:1:-3], lst[30:1:-3])
        self.assertEqual(arr[7:1:-3], lst[7:1:-3])
        self.assertEqual(arr[6:1:-3], lst[6:1:-3])
        self.assertEqual(arr[1:1:-3], lst[1:1:-3])

    def test_slicing(self):
        "Test slicing."
        arr = [0]
        lst = ll.make(arr) or []
        self.subtest_slicing(arr, lst)
        arr = [0, 1]
        lst = ll.make(arr) or []
        self.subtest_slicing(arr, lst)
        arr = [0, 1, 2]
        lst = ll.make(arr) or []
        self.subtest_slicing(arr, lst)
        arr = [0, 1, 2, 3]
        lst = ll.make(arr) or []
        self.subtest_slicing(arr, lst)

        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        lst = ll.make(arr) or []
        self.subtest_slicing(arr, lst)

    def test_middle(self):
        "Test `middle` node function."
        self.assertIsNone(ll.middle(ll.make([])))

        self.assertEqual(1, ll.middle(ll.make([1])).data)
        self.assertEqual(2, ll.middle(ll.make([1, 2])).data)
        self.assertEqual(2, ll.middle(ll.make([1, 2, 3])).data)
        self.assertEqual(3, ll.middle(ll.make([1, 2, 3, 4])).data)

    def test_delete_middle(self):
        "Test `delete_middle` node function."
        self.assertIsNone(ll.delete_middle(ll.make([])))
        self.assertIsNone(ll.delete_middle(ll.make([1])))

        self.assertEqual([1], seq(ll.delete_middle(ll.make([1, 2]))))
        self.assertEqual([1, 3], seq(ll.delete_middle(ll.make([1, 2, 3]))))
        self.assertEqual([1, 2, 4], seq(ll.delete_middle(ll.make([1, 2, 3, 4]))))

    def test_nth(self):
        "Test `nth` function."
        l = ll.make([1, 2, 3, 4])
        self.assertEqual(1, ll.nth(l, 0).data)
        self.assertEqual(4, ll.nth(l, 3).data)
        self.assertEqual(4, ll.nth(l, -1).data)
        self.assertEqual(1, ll.nth(l, -4).data)
        self.assertIsNone(ll.nth(l, 4))
        self.assertIsNone(ll.nth(l, -5))

        e = ll.make([])
        self.assertIsNone(ll.nth(e, 0))
        self.assertIsNone(ll.nth(e, 1000))
        self.assertIsNone(ll.nth(e, -1000))

    def test_insert_sorted(self):
        "Test `insert_sorted`."
        self.assertEqual([1], seq(ll.insert_sorted(ll.make([]), 1)))
        self.assertEqual([1, 2], seq(ll.insert_sorted(ll.make([1]), 2)))
        self.assertEqual([1, 2], seq(ll.insert_sorted(ll.make([2]), 1)))
        self.assertEqual([1, 2, 3], seq(ll.insert_sorted(ll.make([1, 3]), 2)))

    def test_reverse(self):
        "Test `reverse`."
        self.assertIsNone(ll.reverse(ll.make([])))

        self.assertEqual([1], seq(ll.reverse(ll.make([1]))))
        self.assertEqual([2, 1], seq(ll.reverse(ll.make([1, 2]))))
        self.assertEqual([3, 2, 1], seq(ll.reverse(ll.make([1, 2, 3]))))

    def test_dedup(self):
        "Test `dedup` function."
        self.assertIsNone(ll.dedup(ll.make([])))

        self.assertEqual([1], seq(ll.dedup(ll.make([1]))))
        self.assertEqual([1, 2, 3], seq(ll.dedup(ll.make([1, 2, 3]))))
        self.assertEqual([3, 2], seq(ll.dedup(ll.make([3, 2, 3]))))
        self.assertEqual([1, 3], seq(ll.dedup(ll.make([1, 3, 3]))))
        self.assertEqual([1, 3], seq(ll.dedup(ll.make([1, 1, 3]))))

    def test_loop_length(self):
        "Test the `loop_length` function."
        self.assertEqual(0, ll.loop_length(ll.make([])))
        self.assertEqual(0, ll.loop_length(ll.make([1])))
        self.assertEqual(1, ll.loop_length(ll.make([1], 0)))
        self.assertEqual(0, ll.loop_length(ll.make([1, 2, 3])))
        self.assertEqual(1, ll.loop_length(ll.make([1, 2, 3], 2)))
        self.assertEqual(2, ll.loop_length(ll.make([1, 2, 3], 1)))
        self.assertEqual(3, ll.loop_length(ll.make([1, 2, 3], 0)))

    def test_swap_pairs(self):
        "Test `swap_pairs` function."
        self.assertIsNone(ll.swap_pairs(ll.make([])))

        self.assertEqual([1], seq(ll.swap_pairs(ll.make([1]))))
        self.assertEqual([2, 1], seq(ll.swap_pairs(ll.make([1, 2]))))
        self.assertEqual([2, 1, 3], seq(ll.swap_pairs(ll.make([1, 2, 3]))))
        self.assertEqual([2, 1, 4, 3], seq(ll.swap_pairs(ll.make([1, 2, 3, 4]))))

    def test_subtract_lists(self):
        "Test `subtract_lists` function."
        self.assertEqual(
            [8, 8],
            seq(
                ll.subtract_lists(
                    ll.make(list(map(int, "100"))), ll.make(list(map(int, "12")))
                )
            ),
        )
        l = ll.subtract_lists(
            ll.make(list(map(int, "020055383525634518999521060086463321841"))),
            ll.make(list(map(int, "10835173613544430215114275094755963004"))),
        )
        self.assertEqual(
            "9220209912090088784406784991707358837", "".join(map(str, l or []))
        )
