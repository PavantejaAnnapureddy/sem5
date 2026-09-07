# cook your dish here
import sys

MOD = 10**9 + 7

def main():

    data = sys.stdin.buffer.read().split()
    
    if not data:
        return
    nums = list(map(int, data))
    N = nums[0]
    Q = nums[1]
    arr = nums[2:2+N]
    query_start = 2 + N
    
    # Precompute Fibonacci
    max_val = max(arr)
    fib = [0] * (max_val + 2)
    
    if max_val >= 1:
        fib[1] = 1
    if max_val >= 2:
        fib[2] = 1
    
    for i in range(3, max_val + 1):
        fib[i] = (fib[i-1] + fib[i-2]) % MOD
    
    # Prefix sum
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = (prefix[i-1] + fib[arr[i-1]]) % MOD
    
    # Process queries
    output = []
    for i in range(Q):
        L = nums[query_start + 2*i]
        R = nums[query_start + 2*i + 1]
        ans = (prefix[R] - prefix[L-1]) % MOD
        output.append(str(ans))
    
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()