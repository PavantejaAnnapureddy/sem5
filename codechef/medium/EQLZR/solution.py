# cook your dish here
def brute_force(n, a):
    best = 0
    for L in range(n):
        for R in range(L, n):
            b = a[:]
            for i in range(L, R+1):
                b[i] += 1
            score = sum(1 for i in range(n-1) if b[i] == b[i+1])
            best = max(best, score)
    return best