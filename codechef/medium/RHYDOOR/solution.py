# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    doors = 0
    count = 0
    prev = ''
    
    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch
        
        if count == 3:
            doors += 1
            count = 0
    
    print(doors)