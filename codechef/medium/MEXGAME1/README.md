# MEXGAME1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### MEX Game (Easy)

Alice and Bob are playing a game on an array $A$ of $N$ integers. Alice goes first.

On each of their turn, they choose some index $i$ such that $A_i > 0$, and replace it with $A_i - 1$.

Such a move is valid only if the MEX$^{\dagger}$ value of the entire array does not change. The player unable to make a valid move loses.

You are given an array $A$ of $N$ integers. Output $\text{Alice}$ if she wins the game on this array, or $\text{Bob}$ if he does.

$^{\dagger}$ The MEX of an array is the minimal non-negative element not included in the array.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the winner of the game.

### Constraints
- $1 \le T \le 10^4$
- $1 \le N \le 2 \cdot 10^5$
- $0 \le A_i \le 100$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
### Sample 1:
Input
Output

```
4
3
0 3 0
4
0 1 2 3
4
0 0 1 1
1
100

```

```
Alice
Bob
Alice
Alice

```

### Explanation:

 **Test Case 1:**  Alice can make the first move on $2^{nd}$ index to get the array $[0, 2, 0]$, and then Bob can make no further move. $[0, 1, 0]$ would make the MEX $2$ instead of $1$.

 **Test Case 2:**  Alice has no initial valid move to make. Any move changes the MEX.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-30T15:51:18.270Z  

```py
from collections import Counter
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        freq = Counter(a)
        
        m = 0
        while m in freq:
            m += 1
        greater_count = sum(1 for x in a if x > m)
        has_dup = False
        for v in range(1, m):
            if freq.get(v, 0) > 1:
                has_dup = True
                break
        
        if greater_count % 2 == 1 or has_dup:
            results.append("Alice")
        else:
            results.append("Bob")
    
    print('\n'.join(results))

solve()
```

---

[View on CodeChef](https://www.codechef.com/problems/MEXGAME1)