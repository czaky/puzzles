"Puzzles related to board games."

def queens(n: int) -> list:
    "Return a list of queen combinations for an `NxN` board."
    if n <= 0:
        return []
    n4 = n*4
    solutions = []
    s = [0] * n
    def rec(r: int, invalid: int):
        place = 1 | 1 << (n+r) | 1 << (n4-r)
        for c in range(n):
            if not invalid & place:
                s[r] = c + 1
                if r == 0:
                    solutions.append(s[:])
                    return
                rec(r-1, invalid | place)
            place <<= 1
    rec(n-1, 0)
    return sorted(solutions)
