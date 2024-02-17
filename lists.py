"""Puzzles around linked lists."""

from typing import Optional

class Node:  # pylint: disable=too-few-public-methods
    "Linked List Node."
    def __init__(self, data):
        self.data = data
        self.next = None

    def __iter__(self):
        n = self
        while n:
            yield n.data
            n = n.next

def make(l: list, loop: int=-1) -> Optional[Node]:
    """
Make a linked list out of normal Python list `l`.

If `loop` >= 0, add a loop at the end pointing to node `loop`.
"""
    if not l:
        return None
    n = h = Node(l[0])
    ln = None if loop != 0 else n
    for i in range(1, len(l)):
        n.next = Node(l[i])
        n = n.next
        loop -= 1
        if loop == 0:
            ln = n
    if ln:
        n.next = ln
    return h

def middle(head: Node) -> Optional[Node]:
    "Return the middle node of the list starting with `head`."
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def nth(head: Node, n: int) -> Optional[Node]:
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
    nn = Node(value)
    if not head or head.data > value:
        nn.next = head
        return nn
    n = head
    while n.next and n.next.data < value:
        n = n.next
    nn.next = n.next
    n.next = nn
    return head

def reverse(head: Node) -> Optional[Node]:
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

def remove_smaller_nodes_left(h: Node) -> Optional[Node]:
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

def sorted_intersection(a: Node, b: Node) -> Optional[Node]:
    "Intersection of two sorted lists `a` and `b`."
    nh = nn = Node(0)
    while a and b:
        diff = a.data - b.data
        if diff == 0:
            nn.next = nn = Node(a.data)
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
