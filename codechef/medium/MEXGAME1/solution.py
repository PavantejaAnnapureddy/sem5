# cook your dish here
from collections import Counter

def solve(n, a):
    freq = Counter(a)
    m = 0
    while m in freq:
        m += 1
    
    total = 0
    for val, cnt in freq.items():
        if val > m:
            total += cnt * (val - m - 1)
    for v in range(1, m):
        if freq.get(v, 0) > 1:
            total += (freq[v] - 1) * v
    
    return "Alice" if total % 2 else "Bob"