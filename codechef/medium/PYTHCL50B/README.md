# PYTHCL50B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Converting input datatype

Listen

The  **`input()`**  function assumes that the input is a string. This means whatever the user types, whether it is letters, numbers, or special characters,  **`input()`**  directly reads it as a string.

So, if you need to work with numbers, you have to convert the input to an integer or a float. We learned how to convert types in one of our previous lessons. We use the same method to convert the input to an integer:

```
num1 = int(input())
num2 = int(input())
print(num1 + num2)

```

If the user enters $2$ as the value of  **`num1`**  and $3$ as the value of  **`num2`**, the output will be $5$. However, if we don't convert it to an `integer`, the output will be $23$ because  **`input()`**  takes the input as a string, and it will perform string concatenation instead of integer addition.

Just like how we used the int() function to convert input to an integer value, we can read values of any datatype. For example, if you want to read float values, you can use the float() function.

### Task

Write a program which does the following

- Declare an integer variable num
- Try taking a number from the console and assign it to num
- Output the square of num to the console

These are few sample testcases for your reference:

### Sample 1:
Input
Output

```
3
```

```
9
```

### Sample 2:
Input
Output

```
4
```

```
16
```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-09T05:17:35.652Z  

```cpp
num1= int(input())
print(num1*num1)
```

---

[View on CodeChef](https://www.codechef.com/problems/PYTHCL50B)