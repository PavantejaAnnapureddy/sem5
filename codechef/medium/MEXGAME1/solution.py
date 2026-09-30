from collections import Counter

def solve(n, a):
    freq = Counter(a)
    m = 0
    while m in freq:
        m += 1
    greater = sum(1 for x in a if x > m)
    has_dup = False
    for v in range(1, m):
        if freq.get(v, 0) > 1:
            has_dup = True
            break
    
    if greater % 2 == 1 or has_dup:
        return "Alice"
    return "Bob"