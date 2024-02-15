"""Puzzles related to binary (search) trees."""

import math
from collections import deque
from typing import Tuple

class Node:  # pylint: disable=too-few-public-methods
    "Node of a binary tree."
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def height(self):
        "Returns max height of the tree starting from this node."
        return 1 + max(
            self.left.height() if self.left else 0,
            self.right.height() if self.right else 0)

    def __iter__(self):
        # level order (breadth first)
        q = deque([self])
        while q:
            n = q.popleft()
            yield n.data
            _ = n.left and q.append(n.left)
            _ = n.right and q.append(n.right)

def make(s: str) -> Node:
    "Make a binary tree from a string `s`."
    def des(it):
        v = next(it, -1)
        if v < 0:
            return None
        n = Node(v)
        n.left = des(it)
        n.right = des(it)
        return n
    return des(iter(map(int, s.split())))

# Determine if a tree is an ordered BST (may be unbalanced)
def is_bst(root: Node) -> bool:
    "True if `root` is a BST."
    def ordered(n: Node, mn: float, mx: float) -> bool:
        return not n or (
            (mn <= n.data <= mx) and
            ordered(n.left, mn, n.data - 1) and
            ordered(n.right, n.data + 1, mx))
    return ordered(root, -math.inf, math.inf)

def left_view(root: Node) -> list:
    "Return the projected left view of the binary tree from `root`."
    view = []
    def enum(n: Node, level: int):
        if not n:
            return
        if level > len(view):
            view.append(n.data)
        enum(n.left, level + 1)
        enum(n.right, level + 1)
    enum(root, 1)
    return view

def right_view(root: Node) -> list:
    "Return the projected right view of the binary tree from `root`."
    view = []
    def enum(n: Node, level: int):
        if not n:
            return
        if level > len(view):
            view.append(n.data)
        enum(n.right, level + 1)
        enum(n.left, level + 1)
    enum(root, 1)
    return view

def breadth_first(t: Node) -> list:
    """Return the node values in breadth first order."""
    q = deque([t])
    o = []
    while q:
        n = q.popleft()
        o.append(n.data)
        _ = n.left and q.append(n.left)
        _ = n.right and q.append(n.right)
    return o

def spiral_order(t: Node) -> list:
    """
Return the node values in spiral.
Spiral order is alternating from left to right on each level.
"""
    q = deque([t])
    o = []
    lvl = 0
    while q:
        lvl += 1
        ro = []
        for _ in range(len(q)):
            n = q.popleft()
            (ro if lvl%2 else o).append(n.data)
            _ = n.left and q.append(n.left)
            _ = n.right and q.append(n.right)
        o.extend(reversed(ro))
    return o

def balanced(root: Node) -> bool:
    "True if tree at `root` is balanced in height."
    def rank_balance(n: Node) -> Tuple[int, bool]:
        if not n:
            return 0, True
        lr, lb = rank_balance(n.left)
        if not lb:
            return lr + 1, False
        rr, rb = rank_balance(n.right)
        return  max(lr, rr) + 1, lb and rb and abs(lr - rr) <= 1
    return rank_balance(root)[1]

def identical(a: Node, b: Node) -> bool:
    "True if `a` and `b` have identical structure and data."
    return a == b or (
        a and b and
        a.data == b.data and
        identical(a.left, b.left) and
        identical(a.right, b.right))

def mirror(r: Node):
    "Mirror the tree at `r` in place."
    if r:
        r.left, r.right = r.right, r.left
        mirror(r.left)
        mirror(r.right)

def insert(r: Node, value: int) -> Node:
    "Insert `value` into a BST starting at `r`."
    if not r:
        return Node(value)
    if value < r.data:
        r.left = insert(r.left, value)
    elif value > r.data:
        r.right = insert(r.right, value)
    return r
