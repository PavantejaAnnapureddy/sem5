N=int(input().split())
arr=map(int,input().split())
miinus= min(arr[i]-arr[i-1]) for i range (1,N)
print(miinus)
