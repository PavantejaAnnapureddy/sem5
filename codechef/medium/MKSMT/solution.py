import sys

def ok(a, n, X):
    fd = next((i for i in range(n-1) if a[i] > a[i+1]), -1)
    if fd == -1: return True
    ld = next(i for i in range(n-2, -1, -1) if a[i] > a[i+1])
    p = next((i for i in range(n-1) if a[i] > a[i+1]), n-1)
    s = next((i for i in range(n-1, 0, -1) if a[i-1] > a[i]), 0)

    for L in {0, max(0, fd-1), fd, fd+1, p, p+1}:
        if L >= n or (L > 0 and any(a[i] > a[i+1] for i in range(L-1))):
            continue
        S, prev = 0, -1
        for i in range(L, n):
            if a[i] >= X:
                S += a[i] - X; cur = X
            else:
                add = min(S, X - a[i]); cur = a[i] + add; S -= add
            if i == L and L > 0 and a[L-1] > cur: break
            if prev != -1 and cur < prev: break
            prev = cur
            if i >= ld and (i+1 >= n or i+1 >= s) and (i+1 >= n or cur <= a[i+1]):
                return True
    return False

def solve():
    d = sys.stdin.read().split()
    t = int(d[0]); k = 1; out = []
    for _ in range(t):
        n = int(d[k]); k += 1
        a = list(map(int, d[k:k+n])); k += n
        if all(a[i] <= a[i+1] for i in range(n-1)):
            out.append("-1"); continue
        lo, hi, ans = 1, max(a), -1
        while lo <= hi:
            m = (lo + hi) // 2
            if ok(a, n, m): ans = m; lo = m + 1
            else: hi = m - 1
        out.append(str(ans))
    print("\n".join(out))

solve()