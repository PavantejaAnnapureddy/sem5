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
        
        total = 0
        for val, cnt in freq.items():
            if val > m:
                total += cnt * (val - m - 1)
        for v in range(1, m):
            if freq.get(v, 0) > 1:
                total += (freq[v] - 1) * v
        
        if total % 2 == 1:
            results.append("Alice")
        else:
            results.append("Bob")
    
    print('\n'.join(results))

solve()