# cook your dish here
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        x = s.count('R') - s.count('L')
        y = s.count('U') - s.count('D')
        
        possible = False
        for c in s:
            dx = dy = 0
            if c == 'U': dy = -2
            elif c == 'D': dy = 2
            elif c == 'L': dx = 2
            elif c == 'R': dx = -2
            
            if x + dx == 0 and y + dy == 0:
                possible = True
                break
        
        print("YES" if possible else "NO")

solve()