# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    total = prefix[n]
    ans = 0
    for k in range(1, n):
        if 2 * k <= n:
            s_r = total - prefix[n - k]
        else:
            s_r = prefix[k]
        s_b = total - s_r
        ans = max(ans, s_r * (n - k) + s_b * k)
    print(ans)