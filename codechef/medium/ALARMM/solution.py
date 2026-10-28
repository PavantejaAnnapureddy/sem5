# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    alarms = 0
    i = 0
    while i < n:
        if s[i] == '1':
            # Place alarm at rightmost position that covers room i
            pos = min(i + k, n - 1)
            alarms += 1
            # Skip all rooms covered by this alarm: [pos-k, pos]
            # Move i to pos+1 (next uncovered room)
            i = pos + 1
        else:
            i += 1
    
    print(alarms)
    