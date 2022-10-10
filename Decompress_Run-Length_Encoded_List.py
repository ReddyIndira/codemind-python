n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in range(0,n,2):
    a=arr[i]
    b=arr[i+1]
    for i in range(a):
        print(b,end=" ")
    