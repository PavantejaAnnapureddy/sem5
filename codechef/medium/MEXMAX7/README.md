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
**Submitted:** 2026-08-19T16:18:50.136Z  

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
    
    ans = 0
    
    for m in range(N + 1):
        if freq[m] == 0:
            continue
        max_val = m - 1
        if max_val < 0:
            continue
        if max_val >= 0 and freq[max_val] == 0:
            continue
        
        possible = True
        for i in range(m - 1):
            if freq[i] == 0:
                possible = False
                break
        if not possible:
            continue
        
        ways = 1
        for i in range(m - 1):
            ways = (ways * pow(2, freq[i], MOD)) % MOD
        
        ways = (ways * (pow(2, freq[m-1], MOD) - 1)) % MOD
        
        ans = (ans + ways) % MOD
    
    for m in range(N):
        max_val = m + 1
        if freq[m] == 0 or freq[m+1] == 0:
            continue
        
        possible = True
        for i in range(m):
            if freq[i] == 0:
                possible = False
                break
        if not possible:
            continue
        
        if freq[m] > 0:
            continue
        
        ways = 1
        for i in range(m):
            ways = (ways * pow(2, freq[i], MOD)) % MOD
        
        ways = (ways * (pow(2, freq[m+1], MOD) - 1)) % MOD
        
        ans = (ans + ways) % MOD
    
    print(ans)
```

---

[View on CodeChef](https://www.codechef.com/problems/MEXMAX7)