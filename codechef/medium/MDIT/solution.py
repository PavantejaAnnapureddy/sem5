import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))
p = list(map(int, input().split()))

children = [[] for _ in range(n)]
root = p.index(-1)

for i in range(n):
    if p[i] != -1:
        children[p[i] - 1].append(i)

ans = 0
stack = [(root, v[root], v[root])]

while stack:
    node, mn, mx = stack.pop()
    curr = v[node]
    
    ans = max(ans, abs(curr - mn), abs(curr - mx))
    
    new_mn = min(mn, curr)
    new_mx = max(mx, curr)
    
    for child in children[node]:
        stack.append((child, new_mn, new_mx))

print(ans)
