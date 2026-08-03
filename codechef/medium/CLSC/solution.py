N=int(input())
arr= sorted(map(int,input().split()))
miinus= min(arr[i]-arr[i-1] for i  in range(1, N))
print(miinus)
