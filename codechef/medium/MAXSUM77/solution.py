# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    L = n - k
    max_sum = 0
    for i in range(k + 1):
        curr_sum = prefix[i + L] - prefix[i]
        max_sum = max(max_sum, curr_sum)
    
    print(max_sum)