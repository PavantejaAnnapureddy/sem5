# cook your dish here
T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    
    if N <= 3:
        total = N * X
    else:
        total = 3 * X + (N - 3) * Y
    
    print(total)