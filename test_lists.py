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
