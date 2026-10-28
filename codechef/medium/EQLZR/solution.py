# cook your dish here
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    base = sum(1 for i in range(n-1) if a[i] == a[i+1])
    
    best = -10**9
    pref_max_f = -10**9
    for R in range(n):
        # f(R)
        if R == 0:
            fR = 0
        else:
            fR = (1 if a[R-1] == a[R]+1 else 0) - (1 if a[R-1] == a[R] else 0)
        pref_max_f = max(pref_max_f, fR)
        # g(R)
        if R == n-1:
            gR = 0
        else:
            gR = (1 if a[R]+1 == a[R+1] else 0) - (1 if a[R] == a[R+1] else 0)
        best = max(best, pref_max_f + gR)
    
    print(base + best)