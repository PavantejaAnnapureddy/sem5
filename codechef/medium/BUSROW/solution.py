T = int(input())
for _ in range(T):
    N, M, X = map(int, input().split())
    row = (X + M - 1) // M
    print(min(row, N - row + 1))