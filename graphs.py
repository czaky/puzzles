"""Puzzles related to graphs."""

from typing import List
from collections import deque

def breadth_first(adj: List[List[int]], start: int=0) -> List[int]:
    "Traverse the graph breadth first. Return list of nodes."
    q = deque([start])
    v = set([start])
    o = []
    while q:
        n = q.popleft()
        o.append(n)
        for d in adj[n]:
            if not d in v:
                q.append(d)
                v.add(d)
    return o
