import sys

def solve():
    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    K = int(data[1])
    A = list(map(int, data[2:2+N]))
    
    A.sort()
    
    ans = float('inf')
    
    for i in range(N + 1):
        min_h = float('inf')
        max_h = -float('inf')
        
        for j in range(N):
            if j < i:
                if A[j] >= K:
                    h = A[j] - K
                else:
                    h = A[j] + K
            else:
                h = A[j] + K
            
            min_h = min(min_h, h)
            max_h = max(max_h, h)
        
        ans = min(ans, max_h - min_h)
    
    print(ans)

if __name__ == "__main__":
    solve()