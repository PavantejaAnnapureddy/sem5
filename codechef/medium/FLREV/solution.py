# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    initial = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            initial += 1
    
    max_beauty = initial
    
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            max_beauty += 1
            break
    
    print(min(max_beauty, n - 1))