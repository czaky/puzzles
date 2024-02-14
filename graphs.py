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

def depth_first(adj: List[List[int]], start: int=0) -> List[int]:
    "Traverse the graph depth first using stack. Return list of nodes."
    o = []
    v = set()
    s = [start]
    while s:
        n = s.pop()
        if n not in v:
            v.add(n)
            o.append(n)
            s.extend(filter(lambda a: a not in v, reversed(adj[n])))
    return o

def depth_first_r(adj: List[List[int]], start: int=0) -> List[int]:
    "Traverse the graph recursively depth first. Return list of nodes."
    o = []
    v = set()
    def dfs(n: int):
        v.add(n)
        o.append(n)
        for a in adj[n]:
            if not a in v:
                dfs(a)
    dfs(start)
    return o
