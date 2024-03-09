"Puzzles related to board games."

def queens(n: int) -> list:
    "Return a list of queen combinations for an `NxN` board."
    col = [0] * n
    rdg = [0] * 2 * n
    ldg = [0] * 2 * n
    solutions = []
    s = [0] * n
    def rec(r: int):
        for c in range(n):
            if col[c] or rdg[n + c - r] or ldg[c + r]:
                continue
            s[r] = c + 1
            if r == 0:
                solutions.append(s[:])
                return
            col[c] = rdg[n + c - r] = ldg[c + r] = 1
            rec(r-1)
            col[c] = rdg[n + c - r] = ldg[c + r] = 0
    rec(n-1)
    return sorted(solutions)
