t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    s = input().strip()
    for i in range(p):  
        if s[i] == 'R':
            left_reversals += 1
    right_reversals = 0
    for i in range(p - 1, n):  
        if s[i] == 'L':
            right_reversals += 1
    
    print(min(left_reversals, right_reversals))