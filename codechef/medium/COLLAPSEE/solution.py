# cook your dish here
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = [int(data[idx+i]) for i in range(n)]
        idx += n
        total = a[n-1] - a[n-2]
        for i in range(n-2):
            total += abs(a[i])
        out.append(str(total))
    sys.stdout.write('\n'.join(out))

solve()