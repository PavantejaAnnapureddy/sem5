# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    freq = {}
    for num in arr:
        msb = num.bit_length()  
        freq[msb] = freq.get(msb, 0) + 1
    
    print(max(freq.values()))