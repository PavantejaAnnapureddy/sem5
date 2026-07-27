# PRCO

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Palindrome Counter

Given a string $S$, determine the total number of  **non-empty palindromic subsequences**  present in it.

A  **subsequence**  is obtained by deleting zero or more characters from the string such that at least one character remains, without changing the relative order of the remaining characters. For example, `"ace"` is a subsequence of `"abcde"`, whereas `"aec"` is not.

A  **palindrome**  is a string that reads the same forwards and backwards. For example, `"aba"`, `"racecar"`, and `"aa"` are palindromes, while `"ab"` is not.

 **Note:**  Two palindromic subsequences are considered different if they are formed using different indices in the original string, even if they produce the same string.

Print the total number of  **non-empty palindromic subsequences**  modulo $10^9 + 7$.

### Input Format
- A single line containing the string $S$.
### Output Format
- Print a single integer — the total number of non-empty palindromic subsequences in $S$, modulo $10^9 + 7$.
### Constraints
- $1 \le |S| \le 1000$
- $S$ consists only of lowercase English letters.
### Sample 1:
Input
Output

```
abcd
```

```
4
```

### Explanation:

The palindromic subsequences are:

- a, b, c, d
### Sample 2:
Input
Output

```
anna
```

```
9
```

### Explanation:

The palindromic subsequences are:

- a, n, n, a, nn, aa, ana, ana, anna

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T15:29:22.195Z  

```c_cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MOD = 1e9 + 7;

int main() {
    string S;
    cin >> S;
    int n = S.length();
    
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            
            if (S[i] == S[j]) {
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % MOD;
            } else {
                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] + MOD) % MOD;
            }
        }
    }
    
    cout << dp[0][n-1] % MOD << endl;
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/PRCO)