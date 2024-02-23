"Puzzles around matrices."

from typing import List
from functools import lru_cache

def find_sorted(hay: List[List[int]], needle: int) -> bool:
    "True if `needle` is in the sorted `hay` matrix."
    n = len(hay)
    m = len(hay[0])
    i = n-1
    j = 0
    while i >= 0 and j < m:
        c = hay[i][j]
        if c < needle:
            j += 1
        elif c > needle:
            i -= 1
        else:
            return True
    return False

def rotate90cc(m: List[List[int]]):
    "Rotate matrix `m` 90deg counter-clockwise."
    # Transpose
    n = len(m)
    for i in range(n):
        for j in range(i, n):
            m[i][j],m[j][i] = m[j][i],m[i][j]
    # Reverse the rows.
    m.reverse()

def optimum_multiplications(a: List[int]) -> int:
    """
Given a list of matrix sizes (a[i] x a[i+1])
return minimum number of operations.
"""
    @lru_cache(None)
    def sub(i,j):
        return int(i < j and
            min(sub(i,k) + sub(k+1,j) + a[i-1]*a[k]*a[j]
                for k in range(i, j)))
    return sub(1, len(a)-1)
