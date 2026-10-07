# cook your dish here
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()
        
        cnt_a = a.count('1')
        cnt_b = b.count('1')
        
        if cnt_a % 2 == cnt_b % 2:
            print("YES")
        else:
            print("NO")

solve()