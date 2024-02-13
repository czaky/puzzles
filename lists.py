# Puzzles around linked lists.

from typing import Optional

class Node:
    "Linked List Node."
    def __init__(self, data):
        self.data = data
        self.next = None

def make_linked(l: list) -> Optional[Node]:
    "Make a linked list out of normal Python list `l`."
    if not l: return None
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
