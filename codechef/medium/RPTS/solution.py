n, k = map(int, input().split())
s = input().strip()

whites = s[:k].count('W')
min_repaint = whites

for i in range(n - k):
    if s[i] == 'W':
        whites -= 1
    if s[i + k] == 'W':
        whites += 1
    min_repaint = min(min_repaint, whites)

print(min_repaint)