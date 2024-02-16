"Utils for iterators."

from itertools import islice

def skip(it, n: int=1):
    "Skip `n` elements in iterator `it`."
    return islice(it, n, None)
