"""Puzzles related to binary (search) trees."""

import math

class Node:  # pylint: disable=too-few-public-methods
    "Node of a binary tree."
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
    max_level = [-1]
    def enum(n: Node, level: int):
        if not n:
            return
        if level > max_level[0]:
            max_level[0] = level
            view.append(n.data)
        enum(n.left, level + 1)
        enum(n.right, level + 1)
    enum(root, 0)
    return view
