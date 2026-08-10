n = int(input())

p1 = p2 = max_lead = 0
winner = 1

for _ in range(n):
    s, t = map(int, input().split())
    p1 += s
    p2 += t
    
    if abs(p1 - p2) > max_lead:
        max_lead = abs(p1 - p2)
        winner = 1 if p1 > p2 else 2

print(winner, max_lead)