n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(len(arr)):
    if(arr[i]>=a and arr[i]<=b):
        s=s+arr[i]
print(s);