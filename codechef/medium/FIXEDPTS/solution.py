# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == n:
        print("Yes")
    elif k <= n - 2:
        print("Yes")
    else:
        print("No")