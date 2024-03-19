"""Puzzles around linked lists."""

from typing import Optional, Iterable, Any


class ListNode(Iterable):
    "Linked List Node."

    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __iter__(self):
        n = self
        while n:
            yield n.data
            n = n.next


Node = Optional[ListNode]


def make(l: Iterable[Any], loop: int = -1) -> Node:
    """
    Make a linked list out of normal Python list `l`.

    If `loop` >= 0, add a loop at the end pointing to node `loop`.
    """
    if not l:
        return None
    n = h = ListNode(0)
    ln = None
    for e in l:
        n.next = ListNode(e)
        n = n.next
        if loop == 0:
            ln = n
        loop -= 1
    if ln:
        n.next = ln
    return h.next


def pprint(head: Node):
    "Pretty print the linked list starting at `head`."
    if not head:
        return
    n = head
    v = set()
    while n:
        if n in v:
            print(f"-> {n.data}")
            break
        v.add(n)
        print(n.data, end=" ")
        n = n.next


def middle(head: Node) -> Node:
    "Return the middle node of the list starting with `head`."
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def delete_middle(head: Node) -> Node:
    "Delete the middle from the list starting at `head`."
    slow = fast = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    if prev:
        prev.next = slow.next
        return head
    return slow and slow.next


def nth(head: Node, n: int) -> Node:
    """
    Return nth node from the linked list starting at `head`.

    If n is negative, returns the nth node from the end of the list.
    """
    if n >= 0:
        while head and n > 0:
            head = head.next
            n -= 1
        return head

    # from the end
    fast = nth(head, -n - 1)
    if not fast:
        return None
    fast = fast.next
    slow = head
    while fast:
        fast = fast.next
        slow = slow.next
    return slow


def insert_sorted(head: Node, value: int) -> Node:
    "Insert `value` into list starting at `head`. Return new head."
    nn = ListNode(value)
    if not head or head.data > value:
        nn.next = head
        return nn
    n = head
    while n.next and n.next.data < value:
        n = n.next
    nn.next = n.next
    n.next = nn
    return head


def reverse(head: Node) -> Node:
    "Reverse a linked starting at `head`."
    prev = None
    while head:
        prev, head.next, head = head, prev, head.next
    return prev


def dedup(head: Node) -> Node:
    "Remove nodes with duplicate values in the linked list."
    s = set()
    n = head
    while n:
        s.add(n.data)
        while n.next and n.next.data in s:
            n.next = n.next.next
        n = n.next
    return head


def delete_node(n: Node):
    "Remove node without reference to `head`."
    assert n.next
    n.data = n.next.data
    n.next = n.next.next


def remove_smaller_nodes_left(h: Node) -> Node:
    "Remove all nodes from list `h` smaller than any node to the right."
    # Runs in-place at O(N).
    rev = reverse(h)
    mx = 0
    n = rev
    while n:
        mx = max(mx, n.data)
        while n.next and n.next.data < mx:
            n.next = n.next.next
        n = n.next
    return reverse(rev)


def sorted_intersection(a: Node, b: Node) -> Node:
    "Intersection of two sorted lists `a` and `b`."
    nh = nn = ListNode(0)
    while a and b:
        diff = a.data - b.data
        if diff == 0:
            nn.next = nn = ListNode(a.data)
        if diff >= 0:
            a = a.next
        if diff <= 0:
            b = b.next
    return nh.next


def loop_length(head: Node) -> int:
    "Count nodes in a loop. Return 0 if none."
    # detect loop
    slow = head
    fast = head
    loop = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            loop = True
            break
    if not loop:
        return 0
    # measure loop
    c = 1
    fast = fast.next
    while fast != slow:
        c += 1
        fast = fast.next
    return c


def swap_pairs(h: Node) -> Node:
    "Swap pairs of nodes in the `h` list."
    if not h or not h.next:
        return h
    n = h
    nn = n.next
    n3 = nn.next
    # swap
    # h=n->nn->n3
    # h=nn->n->n3
    h = nn
    nn.next = n
    n.next = n3
    while n3 and n3.next:
        # shift
        # nn->n->n3->n4->n5
        #     p->n ->nn->n3
        p, n, nn, n3 = n, n3, n3.next, n3.next.next
        # swap
        # p->n->nn->n3
        # p->nn->n->n3
        p.next = nn
        nn.next = n
        n.next = n3
    return h


def subtract_lists(l1: Node, l2: Node) -> Node:
    "Subtract the smaller from the larger list representing numbers."
    # This exercise uses Node traversal instead of simple arithmetic.

    def compare(l1: Node, l2: Node) -> int:
        "Determine longest/largest list."
        h1, h2 = l1, l2
        while h1 and h2:
            h1, h2 = h1.next, h2.next
        if h2:
            return -1
        if h1:
            return 1

        h1, h2 = l1, l2
        while h1 and h2:
            if h1.data < h2.data:
                return -1
            if h1.data > h2.data:
                return 1
            h1, h2 = h1.next, h2.next
        return 0

    def trim(l: Node) -> Node:
        "Skip leading zeros."
        while l and l.data == 0:
            l = l.next
        return l

    # remove leading zeros
    l1, l2 = trim(l1), trim(l2)

    cmp = compare(l1, l2)
    if cmp == 0:
        return ListNode(0)
    if cmp == -1:
        l1, l2 = l2, l1

    # h1 is longer/larger
    h1 = reverse(l1)
    h2 = reverse(l2)

    d = 0
    r = None
    while h1:
        d = -int(d < 0) + h1.data - (h2.data if h2 else 0)
        n = ListNode(d if d >= 0 else 10 + d)
        n.next = r
        r = n
        h1, h2 = h1.next, h2 and h2.next
    return trim(r) or ListNode(0)
