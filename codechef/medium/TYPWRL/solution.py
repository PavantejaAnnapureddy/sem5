def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        s = input().strip()
        l = input().strip()
        
        hands = ''.join('L' if c in l else 'R' for c in s)
        
        max_count = 1
        count = 1
        for i in range(1, n):
            if hands[i] == hands[i-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        print(max_count)

solve()