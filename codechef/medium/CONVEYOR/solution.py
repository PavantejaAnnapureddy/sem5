t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    s = input().strip()
    left = s[:p].count('R')
    right = s[p-1:].count('L')
    
    print(min(left, right))