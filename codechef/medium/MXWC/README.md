# MXWC

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Maximum Water Container

You are given an array $height$ of length $n$, where $height[i]$ represents the height of a vertical line drawn at position $i$.

Choose  **two different lines**  at indices $i$ and $j$ such that, together with the $x$-axis, they form a container.

The amount of water stored by the container depends on:

- the distance between the two lines, and
- the height of the shorter line.

Find the  **maximum amount of water**  that can be stored by choosing the best pair of lines.

The container  **cannot be tilted**.

### Input Format

The first line contains an integer $n$ — the number of vertical lines. The second line contains $n$ space-separated integers representing the array $height$.

### Output Format

Print a single integer — the maximum amount of water that can be stored.

### Constraints
- $2 \le n \le 10^5$
- $0 \le height[i] \le 10^4$
### Sample 1:
Input
Output

```
9
1 8 6 2 5 4 8 3 7
```

```
49
```

### Explanation:

Choosing the lines at indices $1$ and $8$ gives:

- Width $=8-1=7$
- Height $=\min(8,7)=7$

Therefore, the amount of water stored is:

$$ 7 \times 7=49 $$
### Sample 2:
Input
Output

```
2
1 1
```

```
1
```

### Explanation:

The two lines are one unit apart, and the shorter height is $1$.

Therefore, the amount of water stored is:

$$ 1 \times 1=1 $$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-10T15:01:02.328Z  

```py
# cook your dish here
n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1
max_water = 0

while left < right:
    width = right - left
    min_height = min(height[left], height[right])
    water = width * min_height
    
    max_water = max(max_water, water)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_water)
```

---

[View on CodeChef](https://www.codechef.com/problems/MXWC)