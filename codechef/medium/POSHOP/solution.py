# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    costs = list(map(int, input().split()))
    
    max_spend = max(costs)
    
    for i in range(n):
        for j in range(i + 1, n):
            if costs[i] <= costs[j]:
                max_spend = max(max_spend, costs[i] + costs[j])
    
    print(max_spend)