# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    
    min_cost = float('inf')
    
    for i in range(n):
        for j in range(i+1, n):
            L_i = max(0, i-k)
            R_i = min(n-1, i+k)
            L_j = max(0, j-k)
            R_j = min(n-1, j+k)
            
            if L_i == 0 and R_j == n-1 and R_i + 1 >= L_j:
                min_cost = min(min_cost, c[i] + c[j])
    
    print(-1 if min_cost == float('inf') else min_cost)