
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    dp = [0] * (N + 1)
    dp[1] = 0  
    max_balance = 0
    
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            gain = A[j-1] - j + i
            dp[j] = max(dp[j], dp[i] + gain)
            max_balance = max(max_balance, dp[j])
    
    print(max_balance)