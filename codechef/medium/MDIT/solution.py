
n = int(input())
v = list(map(int, input().split()))
p = list(map(int, input().split()))

mn, mx = [0]*n, [0]*n
ans = 0

for i in range(n):
    if p[i] == -1:
        mn[i] = mx[i] = v[i]
    else:
        j = p[i] - 1
        mn[i] = min(mn[j], v[i])
        mx[i] = max(mx[j], v[i])
        ans = max(ans, abs(v[i]-mn[i]), abs(v[i]-mx[i]))

print(ans)