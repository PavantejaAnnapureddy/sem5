t = int(input())
for _ in range(t):
    A, B, P, Q, R = map(int, input().split())
    
    ans = float('inf')
    
    for d in range(min(A, B) + 1):
        rem_x = A - d
        rem_y = B - d
        
        cost_x = ((rem_x + 1) // 2) * P
        cost_y = ((rem_y + 1) // 2) * Q
        
        ans = min(ans, d * R + cost_x + cost_y)
    
    print(ans)