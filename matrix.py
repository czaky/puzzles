"Puzzles around matrices."

#from collections import Counter
from typing import List #, Optional
# from functools import reduce
#from operator import mul
#from itertools import accumulate, islice

def find_sorted(hay: List[List[int]], needle: int) -> bool:
    "True if `needle` is in the `hay` matrix."
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
