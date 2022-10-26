n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
c=0
for i in range(len(arr)):
    if(arr[i]>=a and arr[i]<=b):
        k.append(arr[i])
        c=1
if(c==0):
    print("-1")
else:
    print(min(k))
