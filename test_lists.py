"""Test module for the linked lists puzzles."""
import unittest
import lists as ll


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

        self.assertEqual([1], list(ll.delete_middle(ll.make([1, 2]))))
        self.assertEqual([1, 3], list(ll.delete_middle(ll.make([1, 2, 3]))))
        self.assertEqual(
            [1, 2, 4], list(ll.delete_middle(ll.make([1, 2, 3, 4]))))

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
        self.assertEqual([1], list(ll.insert_sorted(ll.make([]), 1)))
        self.assertEqual([1, 2], list(ll.insert_sorted(ll.make([1]), 2)))
        self.assertEqual([1, 2], list(ll.insert_sorted(ll.make([2]), 1)))
        self.assertEqual(
            [1, 2, 3], list(ll.insert_sorted(ll.make([1, 3]), 2)))

    def test_reverse(self):
        "Test `reverse`."
        self.assertIsNone(ll.reverse(ll.make([])))

        self.assertEqual([1], list(ll.reverse(ll.make([1]))))
        self.assertEqual([2, 1], list(ll.reverse(ll.make([1, 2]))))
        self.assertEqual([3, 2, 1], list(ll.reverse(ll.make([1, 2, 3]))))

    def test_dedup(self):
        "Test `dedup` function."
        self.assertIsNone(ll.dedup(ll.make([])))

        self.assertEqual([1], list(ll.dedup(ll.make([1]))))
        self.assertEqual([1, 2, 3], list(ll.dedup(ll.make([1, 2, 3]))))
        self.assertEqual([3, 2], list(ll.dedup(ll.make([3, 2, 3]))))
        self.assertEqual([1, 3], list(ll.dedup(ll.make([1, 3, 3]))))
        self.assertEqual([1, 3], list(ll.dedup(ll.make([1, 1, 3]))))

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

        self.assertEqual([1], list(ll.swap_pairs(ll.make([1]))))
        self.assertEqual([2, 1], list(ll.swap_pairs(ll.make([1, 2]))))
        self.assertEqual([2, 1, 3], list(ll.swap_pairs(ll.make([1, 2, 3]))))
        self.assertEqual(
            [2, 1, 4, 3], list(ll.swap_pairs(ll.make([1, 2, 3, 4]))))


    def test_subtract_lists(self):
        "Test `subtract_lists` function."
        self.assertEqual(
            [8, 8], list(ll.subtract_lists(
                ll.make(list(map(int, '100'))),
                ll.make(list(map(int, '12')))))
        )
        self.assertEqual(
            [9, 2, 2, 0, 2, 0, 9, 9, 1, 2, 0, 9, 0, 0, 8, 8, 7, 8,
            4, 4, 0, 6, 7, 8, 4, 9, 9, 1, 7, 0, 7, 3, 5, 8, 8, 3, 7],
            list(ll.subtract_lists(
                ll.make(list(map(int, '020055383525634518999521060086463321841'))),
                ll.make(list(map(int, '10835173613544430215114275094755963004')))))
        )
