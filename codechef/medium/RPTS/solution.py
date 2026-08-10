n, k = map(int, input().split())
s = input().strip()

min_repaint = float('inf')

for i in range(n - k + 1):
    whites = 0
    for j in range(i, i + k):
        if s[j] == 'W':
            whites += 1
    min_repaint = min(min_repaint, whites)

print(min_repaint)