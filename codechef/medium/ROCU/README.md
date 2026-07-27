# ROCU

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Maximize Wood Value

A carpenter has a wooden plank of length $N$ and an array $price$ of size $N$, where $price_i$ denotes the selling price of a wooden piece of length $i$.

The carpenter may cut the plank into any number of smaller pieces or choose not to cut it at all. Every piece produced must have an integer length, and the sum of the lengths of all pieces must be exactly $N$.

Determine the  **maximum revenue**  the carpenter can earn by choosing an optimal way to cut the plank.

### Input Format
- The first line contains an integer $N$, the length of the plank.
- The second line contains $N$ space-separated integers, where the $i^{th}$ integer denotes the selling price of a plank of length $i$.
### Output Format
- Print a single integer — the maximum revenue obtainable.
### Constraints
- $1 \le N \le 10^3$
- $1 \le price_i \le 10^6$
### Sample 1:
Input
Output

```
4
1 5 8 9
```

```
10
```

### Explanation:

One optimal way is to cut the plank into two pieces of length $2$.

Revenue = $5 + 5 = 10$, which is greater than selling the plank as a single piece for $9$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T15:26:43.387Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
int c;
cin>>c;
vector<int> v(c);

}

```

---

[View on CodeChef](https://www.codechef.com/problems/ROCU)