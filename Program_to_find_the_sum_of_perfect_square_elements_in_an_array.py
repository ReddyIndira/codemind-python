n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(0,n):
    l=1
    while l*l<=arr[i]:
        if l*l==arr[i]:
            s=s+arr[i]
        l+=1
print(s)
    