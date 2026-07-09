# PYTHCL50C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Multiple string inputs

Listen

You've seen how to use the  **`input()`**  function to take input multiple times, accepting one value per line. However, sometimes you need to accept multiple inputs in a single line. To do this, you can use the  **`split()`**  function.

For example, if the user inputs the following:

```
Good Great Awesome

```

You can read these inputs like this:

```
a, b, c = input().split()

```

The  **`split()`**  function breaks this single line of input into multiple parts. By default,  **`split()`**  divides the input based on spaces, so each word separated by a space is treated as an independent input and stored in different variables.

### Task
- Write a program that accepts four words from the user in a single line and prints them in reverse order.
### Sample 1:
Input
Output

```
Air Water Earth Fire
```

```
Fire Earth Water Air
```

### Sample 2:
Input
Output

```
coffee headphone swiss chocolate
```

```
chocolate swiss headphone coffee
```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-09T05:36:30.328Z  

```cpp
#
words = input().split()
print(' '.join(reversed(words)))
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL50C)