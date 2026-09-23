# cook your dish here
import sys

def canMakeSorted(A, X):

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        A = list(map(int, data[idx:idx+n])); idx += n
        
        if all(A[i] <= A[i+1] for i in range(n-1)):
            print(-1)
            continue
        lo, hi = 1, max(A)
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if canMakeSorted(A, mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print(ans)

solve()