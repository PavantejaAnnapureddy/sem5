
T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()
    
    ca = A.count('a')
    da = B.count('a')
    
    if ca + da == N:
        print("YES")
    else:
        print("NO")