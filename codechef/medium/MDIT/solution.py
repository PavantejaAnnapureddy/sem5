n = int(input())
v = list(map(int, input().split()))
p = list(map(int, input().split())
children = [[] for _ in range(n)]
root = -1

for i in range(n):
    if p[i] == -1:
        root = i
    else:
        children[p[i]-1].append(i)
ans = 0
stack = [(root, v[root], v[root])]

while stack:
    node, mn, mx = stack.pop()
    ans = max(ans, abs(v[node]-mn), abs(v[node]-mx))
    
    new_mn = min(mn, v[node])
    new_mx = max(mx, v[node])
    
    for child in children[node]:
        stack.append((child, new_mn, new_mx))

print(ans)