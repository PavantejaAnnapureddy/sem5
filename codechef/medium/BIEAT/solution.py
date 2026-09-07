# cook your dish here
MOD = 10**9 + 7
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

max_val = max(arr)
fib = [0] * (max_val + 2)
if max_val >= 1:
    fib[1] = 1
if max_val >= 2:
    fib[2] = 1

for i in range(3, max_val + 1):
    fib[i] = (fib[i-1] + fib[i-2]) % MOD
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    fib_value = fib[arr[i-1]]
    prefix[i] = (prefix[i-1] + fib_value) % MOD
for _ in range(Q):
    L, R = map(int, input().split())
    result = (prefix[R] - prefix[L-1]) % MOD
    print(result)