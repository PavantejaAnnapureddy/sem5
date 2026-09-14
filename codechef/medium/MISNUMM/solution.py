# cook your dish here
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

freq_a = {}
freq_b = {}

for num in a:
    freq_a[num] = freq_a.get(num, 0) + 1

for num in b:
    freq_b[num] = freq_b.get(num, 0) + 1

missing = []
for num in freq_b:
    if freq_a.get(num, 0) < freq_b[num]:
        missing.append(num)

missing.sort()

if missing:
    print(' '.join(map(str, missing)))
else:
    print(-1)