# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n <= k - 1:
        print(n)
    else:
        q, r = divmod(n, k - 1)
        if r == 0:
            print(q * k - 1)
        else:
            print(q * k + r)