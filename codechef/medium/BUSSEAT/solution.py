# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k <= n:
        print(0)
    else:
        print(2 * (k - n))