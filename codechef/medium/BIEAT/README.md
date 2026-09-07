# BIEAT

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Bit Eater

You are given an array $A$ of $N$ non-negative integers and an integer $M$.

For each element, remove its $M$  **least significant bits**  from its binary representation. This is equivalent to replacing $A_i$ with $\left\lfloor \frac{A_i}{2^M} \right\rfloor$.

If all bits of a number are removed, its resulting value becomes $0$.

Print the resulting array after applying this operation to every element.

### Input Format

The first line contains an integer $N$ — the size of the array.

The second line contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

The third line contains an integer $M$ — the number of least significant bits to remove.

### Output Format

Print $N$ space-separated integers representing the array after removing the $M$ least significant bits from every element.

### Constraints
- $1 \le N \le 10^5$
- $0 \le A_i \le 10^9$
- $0 \le M \le 30$
### Sample 1:
Input
Output

```
5
12 25 7 32 1
1
```

```
6 12 3 16 0
```

### Explanation:

Removing $1$ least significant bit from each number gives:

$12 \rightarrow 6,\ 25 \rightarrow 12,\ 7 \rightarrow 3,\ 32 \rightarrow 16,\ 1 \rightarrow 0$

### Sample 2:
Input
Output

```
4
15 8 3 0
4
```

```
0 0 0 0
```

### Explanation:

Each number has at most $4$ significant bits, so removing $4$ least significant bits makes every resulting value $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-07T14:43:07.567Z  

```py
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
```

---

[View on CodeChef](https://www.codechef.com/problems/BIEAT)