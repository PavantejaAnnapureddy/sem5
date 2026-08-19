# cook your dish here
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    total_sum = 0
    max_seen = 0
    answer = 0
    
    for i in range(N):
        total_sum += A[i]
        max_seen = max(max_seen, A[i])
        
        if total_sum - max_seen <= K:
            answer = i + 1
        else:
            break
    
    print(answer)