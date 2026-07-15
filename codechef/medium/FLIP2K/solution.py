# cook your dish here
import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        
        zeros = s.count('0')
        ones = n - zeros
        
        if zeros < k or ones < k:
            print(s)
            continue
        cnt = [0] * k
        for i, c in enumerate(s):
            if c == '0':
                cnt[i % k] += 1
        ans = ['1'] * n
        placed = 0
        for i in range(n):
            if placed < zeros:
              
                ans[i] = '0'
                placed += 1
            else:
                break
        
        print(''.join(ans))

if __name__ == "__main__":
    solve()