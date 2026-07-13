# Fizz Buzz

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `n`, return  *a string array* `answer` *(**1-indexed**) where* :

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.

 

 **Example 1:** 

```
Input: n = 3
Output: ["1","2","Fizz"]

```

 **Example 2:** 

```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

```

 **Example 3:** 

```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

```

 

 **Constraints:** 

- 1 <= n <= 104

## Solution

**Language:** C++  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 11.7 MB (beats 47.07%)  
**Submitted:** 2026-07-13T09:48:53.558Z  

```cpp
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        
        for (int i = 1; i <= n; i++) {
            answer.push_back(
                (i % 15 == 0) ? "FizzBuzz" :
                (i % 3 == 0)  ? "Fizz" :
                (i % 5 == 0)  ? "Buzz" :
                to_string(i)
            );
        }
        
        return answer;
    }
};
```

---

[View on LeetCode](https://leetcode.com/problems/fizz-buzz/)