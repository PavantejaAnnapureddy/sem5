# MISNUMM

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Missing Numbers

Chef has an original array $B$. After some elements are removed and the remaining elements are rearranged, it becomes array $A$.

Find all numbers whose  **frequency in $A$ is smaller than their frequency in $B$**. Print each such number  **once**, in increasing order.

It is possible that no elements were removed.

### Input Format
- The first line contains an integer $N$, the length of $A$.
- The second line contains $N$ integers $A_1,A_2,\ldots,A_N$.
- The third line contains an integer $M$, the length of $B$.
- The fourth line contains $M$ integers $B_1,B_2,\ldots,B_M$.
### Output Format

Print the missing numbers in increasing order, separated by spaces. If no numbers are missing, print $-1$.

### Constraints
- $1 \le N \le M \le 100$
- $1 \le A_i,B_i \le 10^4$
- $\max(B)-\min(B) \le 100$
- For every value, its frequency in $A$ does not exceed its frequency in $B$.
### Sample 1:
Input
Output

```
6
7 2 5 3 5 3
8
7 2 5 4 6 3 5 3
```

```
4 6
```

### Explanation:

Numbers $4$ and $6$ each occur once in $B$ and do not occur in $A$. Every other number has the same frequency in both arrays.

### Sample 2:
Input
Output

```
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
```

```
204 205 206
```

### Explanation:

Each of $204$, $205$, and $206$ occurs three times in $B$ but only twice in $A$. Each missing number is printed once.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T15:22:33.727Z  

```py
# cook your dish here
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

freq_a = {}
freq_b = {}

for num in a:
    freq_a[num] = freq_a.get(num, 0) + 1

for num in b:
    freq_b[num] = freq_b.get(num, 0) + 1

missing = []
for num in freq_b:
    if freq_a.get(num, 0) < freq_b[num]:
        missing.append(num)

missing.sort()

if missing:
    print(' '.join(map(str, missing)))
else:
    print(-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/MISNUMM)