T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    
    ans = float('inf')
    for m in range(1, 1000):

        sum_sq = m * (m + 1) * (2 * m + 1) // 6
        revenue = Y * sum_sq
        if revenue > m * X:
            ans = min(ans, m)
            continue
        need = m * X - revenue
        per_day = Y * m * m
        extra_days = (need + per_day - 1) // per_day 
        ans = min(ans, m + extra_days)
    
    print(ans)