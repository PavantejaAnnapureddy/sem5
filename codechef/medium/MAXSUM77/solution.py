t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    L = n - k
    window_sum = sum(arr[:L])
    max_sum = window_sum
    for i in range(L, n):
        window_sum += arr[i] - arr[i - L]
        max_sum = max(max_sum, window_sum)
    
    print(max_sum)