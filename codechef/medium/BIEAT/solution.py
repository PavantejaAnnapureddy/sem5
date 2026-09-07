import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    
    if not data:
        return
    N = int(data[0])
    Q = int(data[1])

    arr = []
    idx = 2
    for i in range(N):
        arr.append(int(data[idx]))
        idx += 1
    
    # Find maximum value in array
    max_val = max(arr)
    
    # Precompute Fibonacci numbers up to max_val
    fib = [0] * (max_val + 2)
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
    output = []
    for _ in range(Q):
        L = int(data[idx])
        R = int(data[idx + 1])
        idx += 2
        
        result = (prefix[R] - prefix[L-1]) % MOD
        output.append(str(result))
    
    # Print all answers at once
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()