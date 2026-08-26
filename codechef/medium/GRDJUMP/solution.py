# cook your dish here
t = int(input())
for _ in range(t):
    A, B, P, Q, R = map(int, input().split())
    
    min_cost = float('inf')
    
    for x in range(A + 1):
        for y in range(B + 1):
            cost = 0
            
            rem_x = A - x
            rem_y = B - y
            
            cost += (rem_x // 2) * P + (rem_x % 2) * P
            cost += (rem_y // 2) * Q + (rem_y % 2) * Q
            
            min_cost = min(min_cost, cost + x * R)
    
    print(min_cost)