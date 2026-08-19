# MEXMAX7

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Mex and Max

You are given an array $A$ containing $N$ integers. Find the number of non-empty subsequences $B$ of $A$ such that:

- $|\text{mex}(B) - \max(B)| \le 1$

Here, $\text{mex}(B)$ represents the minimum non-negative integer not present in $B$, and $\max(B)$ represents the maximum element of $B$.

Since the answer may be large, find it modulo $998244353$. $2$ subsequences are different if the indices chosen are different, even if the elements are the same.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the number of subsequences satisfying $|\text{mex}(B) - \max(B)| \le 1$ modulo $998244353$.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $0 \le A_i \le N$
### Sample 1:
Input
Output

```
5
3
0 1 2
6
2 2 1 0 0 4
5
0 1 2 3 4
5
1 1 1 2 2
3
3 3 3

```

```
5
34
9
7
0
```

### Explanation:

 **Test Case 1:**  The following are the good subsequences : $[0], [0, 1], [0, 1, 2], [1], [0, 2]$. For example, the first has a $\text{MEX}$ of $1$ and a $\max$ of $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T16:23:15.447Z  

```py
# cook your dish here
MOD = 998244353

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    freq = [0] * (N + 2)
    for x in A:
        freq[x] += 1
    
    pow2 = [1] * (N + 2)
    for i in range(1, N + 2):
        pow2[i] = (pow2[i - 1] * 2) % MOD
    
    ways = [0] * (N + 2)
    for i in range(N + 2):
        ways[i] = (pow2[freq[i]] - 1) % MOD
    
    pref = [1] * (N + 2)
    pref[0] = ways[0]
    for i in range(1, N + 2):
        pref[i] = (pref[i - 1] * ways[i]) % MOD
    
    ans = 0
    
    for m in range(1, N + 1):
        prod = pref[m - 1]
        ans = (ans + prod) % MOD
    
    for m in range(0, N):
        prod = pref[m - 1] if m > 0 else 1
        prod = (prod * ways[m + 1]) % MOD
        ans = (ans + prod) % MOD
    
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/MEXMAX7)