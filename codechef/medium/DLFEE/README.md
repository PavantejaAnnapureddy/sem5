# DLFEE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Delivery Fee

You are ordering food that costs $A$ rupees.

Normally, a delivery fee of $B$ rupees is added to the order. However, if the food cost is  **at least $K$ rupees**, the delivery is free.

Find the  **total amount**  you need to pay.

### Input Format
- The first line contains three space-separated integers $A$, $B$, and $K$ — the food cost, the delivery fee, and the minimum food cost required for free delivery.
### Output Format
- Print a single integer — the total amount you need to pay.
### Constraints
- $1 \le A,B,K \le 10^4$
### Sample 1:
Input
Output

```
450 50 500
```

```
500
```

### Explanation:

The food cost is $450$, which is less than $500$.

Therefore, the delivery fee of $50$ is added.

The total amount is $450+50=500$.

### Sample 2:
Input
Output

```
600 50 500
```

```
600
```

### Explanation:

The food cost is at least $500$, so the delivery is free.

Therefore, the total amount is $600$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-10T14:38:22.489Z  

```py
# cook your dish here
d,f,g= int(input(),split())
if(d>g){
    print(d)
}
else{
    print(d+f)
}

```

---

[View on CodeChef](https://www.codechef.com/problems/DLFEE)