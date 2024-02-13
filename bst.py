# Puzzles related to binary search trees.abs

import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Determine if a tree is an ordered BST (may be unbalanced)
def isBST(root: Node) -> bool:
    "True if `root` is a BST."
    def ordered(n: Node, mn, mx) -> bool:
        if not n: return True
        return not n or (
            (mn <= n.data <= mx) and
            ordered(n.left, mn, n.data + 1) and
            ordered(n.right, n.data + 1, mx))
    return ordered(root, -math.inf, math.inf)