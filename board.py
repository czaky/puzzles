"Puzzles related to board games."

def queens(n: int) -> list:
    "Return a list of queen combinations for an `NxN` board."
    sols = []
    s = [0] * n
    def rec(r: int, invalid: int):
        place = 1 | 1 << (n+r) | 1 << (n*4-r)
        for s[r] in range(1, n+1):
            invalid & place or (
                rec(r-1, invalid | place) if r > 0
                else sols.append(s[:]))
            place <<= 1
    n > 0 and rec(n-1, 0)
    return sols
