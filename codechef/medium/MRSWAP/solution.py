# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    for i in range(N):
        max_sum += max(arr[i], arr[2*N - 1 - i])
    print(max_sum)