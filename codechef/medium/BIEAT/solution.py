import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    N = int(data[0])
    Q = int(data[1])
    
    # Read array
    arr = []
    idx = 2
    max_val = 0
    for i in range(N):
        val = int(data[idx])
        arr.append(val)
        if val > max_val:
            max_val = val
        idx += 1
    
    # Precompute Fibonacci numbers up to max_val
    # fib[0] = 0, fib[1] = 1, fib[2] = 1
    fib = [0] * (max_val + 1)
    
    if max_val >= 1:
        fib[1] = 1
    if max_val >= 2:
        fib[2] = 1
    
    for i in range(3, max_val + 1):
        fib[i] = (fib[i-1] + fib[i-2]) % MOD
    
    # Build prefix sum
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = (prefix[i-1] + fib[arr[i-1]]) % MOD
    
    # Process queries
    out = []
    for _ in range(Q):
        L = int(data[idx])
        R = int(data[idx + 1])
        idx += 2
        
        ans = (prefix[R] - prefix[L-1]) % MOD
        out.append(str(ans))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()