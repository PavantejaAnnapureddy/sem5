t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    first_z = -1
    for i in range(n):
        if s[i] == 'z':
            first_z = i
            break
    if first_z != -1:
        i = first_z
        while i < n and s[i] == 'z':
            s[i] = 'a'
            i += 1
    
    print(''.join(s))