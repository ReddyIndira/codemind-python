n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
arr.reverse()
b=[]
for i in range(len(arr)):
    if(i%2!=0):
        b.append(arr[i])
        b.append(arr[i-1])
if(n%2==1):
    b.append(arr[n-1])
print(*b)
    