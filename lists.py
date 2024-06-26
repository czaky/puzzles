"""Puzzles around linked lists."""

from __future__ import annotations

from collections.abc import Sequence
from itertools import islice
from typing import Any, Iterable, Iterator, Optional


class ListNode(Sequence):
    """Linked List Node."""

    def __init__(self, data: Any) -> None:
        """Create a ListNode using `data` as node value.

        Parameters
        ----------
        data : Any
            Value assigned to this node.

        """
        self.data = data
        self.next: Node = None

    def __iter__(self) -> Iterator:
        """Iterate over the list node values."""
        n = self
        while n is not None:
            yield n.data
            n = n.next

    def __bool__(self) -> bool:
        """Return True."""
        return True

    def __len__(self) -> int:
        """Compute the length starting at this node."""
        n: Node = self.next
        c = 1
        while n is not None:
            c += 1
            n = n.next
        return c

    def __contains__(self, x: object) -> bool:
        """Return True if x is contained in this list."""
        n = self
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False

    def __getitem__(self, i: int | slice) -> Any:
        """Return an element or a slice of this List."""
        n = self
        if isinstance(i, int):
            while n is not None and i > 0:
                n = n.next
                i -= 1
            if n is None:
                msg = "list index out of range"
                raise IndexError(msg)
            return n.data
        if isinstance(i, slice):
            start, stop, step = i.indices(len(self))
            if step < 0:
                ln = len(range(start, stop, step)) - 1
                start, stop = start + ln * step, start - step
            result = list(islice(self, start, stop, abs(step)))
            if step < 0:
                result.reverse()
            return result
        return None

    def __str__(self) -> str:
        """Return string representation of this node."""
        if self.next:
            return f"({self.data}, ...)"
        return f"({self.data},)"

    def append(self, n: Node) -> None:
        """Append node `n` to this list."""
        self.next = n


Node = Optional[ListNode]


def make(it: Iterable[Any], loop: int = -1) -> Node:
    """Make a linked list out of normal Python list `l`.

    If `loop` >= 0, add a loop at the end pointing to node `loop`.
    """
    if not it:
        return None
    n = h = ListNode(0)
    ln = None
    for e in it:
        n.next = ListNode(e)
        n = n.next
        if loop == 0:
            ln = n
        loop -= 1
    if ln:
        n.next = ln
    return h.next


def pprint(head: Node) -> None:
    """Pretty print the linked list starting at `head`."""
    if not head:
        return
    n = head
    v = set()
    while n:
        if n in v:
            print(f"-> {n.data}")  # noqa: T201
            break
        v.add(n)
        print(n.data, end=" ")  # noqa: T201
        n = n.next


def middle(head: Node) -> Node:
    """Return the middle node of the list starting with `head`."""
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def delete_middle(head: Node) -> Node:
    """Delete the middle from the list starting at `head`."""
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
    """Return nth node from the linked list starting at `head`.

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
    """Insert `value` into list starting at `head`. Return new head."""
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
    """Reverse a linked starting at `head`."""
    prev = None
    while head:
        prev, head.next, head = head, prev, head.next
    return prev


def dedup(head: Node) -> Node:
    """Remove nodes with duplicate values in the linked list."""
    s = set()
    n = head
    while n:
        s.add(n.data)
        while n.next and n.next.data in s:
            n.next = n.next.next
        n = n.next
    return head


def delete_node(n: Node) -> None:
    """Remove node without reference to `head`."""
    if n.next:
        n.data = n.next.data
        n.next = n.next.next
    else:
        msg = "Cannot erase node value with next node."
        raise IndexError(msg)


def remove_smaller_nodes_left(h: Node) -> Node:
    """Remove all nodes from list `h` smaller than any node to the right."""
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
    """Intersection of two sorted lists `a` and `b`."""
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
    """Count nodes in a loop. Return 0 if none."""
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

def print_loop(head: Node) -> None:
    """Print nodes in a loop."""
    # detect loop
    slow = head
    fast = head
    loop = False
    print("[", end="")  # noqa: T201
    while fast and fast.next:
        print(slow.data, end=", ")  # noqa: T201
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            loop = True
            break
    if loop:
        print(fast.data, end="*, ")  # noqa: T201
        fast = fast.next
        while fast != slow:
            print(fast.data, end=", ")  # noqa: T201
            fast = fast.next
    print("]")  # noqa: T201


def swap_pairs(h: Node) -> Node:
    """Swap pairs of nodes in the `h` list."""
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


def add_lists(l1: Node, l2: Node) -> Node:
    """Add two numbers represented as linked lists."""
    n1 = reverse(l1)
    n2 = reverse(l2)

    h = s = ListNode(0)

    c = 0
    while n1 or n2:
        d = c
        if n1:
            d += n1.data
            n1 = n1.next
        if n2:
            d += n2.data
            n2 = n2.next
        c = d // 10
        s.next = ListNode(d % 10)
        s = s.next

    if c != 0:
        s.next = ListNode(c)
        s = s.next

    s = reverse(h.next)
    while s and s.data == 0:
        s = s.next
    h.next = None
    return s or h


def subtract_lists(l1: Node, l2: Node) -> Node:
    """Subtract the smaller from the larger list representing numbers."""
    # This exercise uses Node traversal instead of simple arithmetic.

    def compare(l1: Node, l2: Node) -> int:
        """Determine longest/largest list."""
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

    def trim(n: Node) -> Node:
        """Skip leading zeros."""
        while n and n.data == 0:
            n = n.next
        return n

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


def merge_sort(h: Node) -> Node:
    """Merge sort a linked list by editing the pointers."""
    if h is None or h.next is None:
        return h
    # split
    m = f = h
    while f.next and f.next.next:
        m = m.next
        f = f.next.next
    n = m.next
    m.next = None
    # n.prev = None
    # sort
    h1 = merge_sort(h)
    h2 = merge_sort(n)
    h = n = None
    # merge
    while h1 and h2:
        if h1.data < h2.data:
            nn = h1
            h1 = h1.next
        else:
            nn = h2
            h2 = h2.next

        # nn.prev = n
        if n:
            n.next = n = nn
        else:
            h = n = nn
    if not n:
        return h1 or h2
    if h1:
        n.append(h1)
    elif h2:
        n.append(h2)

    return h


def rearrange_alphabet_list(h: Node) -> Node:
    """Rearrange vovel nodes first.

    Given a linked list containing letters of Latin alphabet,
    rearrange the nodes so that all the vowels come first.
    Otherwise, honor the order of the elements.

    Parameters
    ----------
    h : Node
        Linked list containing the Latin characters.

    Returns
    -------
    Node
        Same list just with all the vowels first.

    """
    vh = v = None
    ch = c = None
    n = h
    while n:
        if n.data in "aeiou":
            if v:
                v.next = n
                v = n
            else:
                vh = v = n
        elif c:
            c.next = n
            c = n
        else:
            ch = c = n
        n = n.next
    if c:
        c.next = None
    if vh:
        v.next = ch
        return vh
    return ch

def reverse_groups(n: Node, k: int) -> Node:
    """Reverse the linked list starting at `n` in groups of `k` nodes.

    Parameters
    ----------
    n : Node
        Head node of the linked list.
    k : int
        Number of nodes to be reversed in each group.

    Returns
    -------
    Node
        The head node of the first reversed group.

    """

    def rev(n: Node) -> tuple[Node, Node]:
        """Return: the head of the reversed group, next node after the group."""
        prev = None
        g = k
        while n and g:
            prev, n.next, n = n, prev, n.next
            g -= 1
        return prev, n

    if n and k > 0:
        h, n, prev = *rev(n), n
        while n:
            prev.next, n, prev = *rev(n), n
        return h
    return n
