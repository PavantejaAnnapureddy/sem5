N = int(input())
A = list(map(int, input().split()))
M = int(input())

print(*[x >> M for x in A])