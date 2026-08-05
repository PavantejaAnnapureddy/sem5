T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = -10**9
    
    dp[1] = 0
    ans = 0
    
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            dp[j] = max(dp[j], dp[i] + A[j-1] - j + i)
            ans = max(ans, dp[j])
    
    print(ans)
