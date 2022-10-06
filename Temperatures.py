n=int(input())
arr=list(map(int,input().split()))
c=0
max=0
for i in range(0,n):
    c=0
    for j in range(i+1,n):
        if(arr[i]<arr[j] and i!=j):
            c+=1
            break
        else:
            c+=1
            if j==n-1:
                c=0
                break
    print(c,end=" ")