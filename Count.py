n=int(input())
arr=list(map(int,input().split()))
c=0
d=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        c+=1
    else:
        d+=1
print(c,d,end="")