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

def make(l: list) -> Optional[Node]:
    "Make a linked list out of normal Python list `l`."
    if not l:
        return None
    n = h = Node(l[0])
    for i in range(1, len(l)):
        n.next = Node(l[i])
        n = n.next
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
