# cook your dish here
N, K = map(int, input().split())
A = list(map(int, input().split()))

threshold = 2 * K
sum_value = 0

for i in range(0, N, 2):  # step by 2 to get even indices
    if A[i] > threshold:
        sum_value += A[i]

print(sum_value)