from collections import Counter
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        freq = Counter(a)
        
        m = 0
        while m in freq:
            m += 1
        greater_count = sum(1 for x in a if x > m)
        has_dup = False
        for v in range(1, m):
            if freq.get(v, 0) > 1:
                has_dup = True
                break
        
        if greater_count % 2 == 1 or has_dup:
            results.append("Alice")
        else:
            results.append("Bob")
    
    print('\n'.join(results))

solve()