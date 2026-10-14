# cook your dish here
import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        k = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n
        
        a.sort()
        max_val = a[-1]
        min_pair_sum = a[0] + a[1]
        ans = max(max_val, min_pair_sum)
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()