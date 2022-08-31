n=int(input())
arr=list(map(int,input().split()))
c=0
if arr[0]<arr[1]:
    for i in range(n-1):
        if i%2==0 and arr[i]<arr[i+1]:
            c+=1
        if i%2!=0 and arr[i]>arr[i+1]:
            c+=1
    if c==n-1:
        print("yes")
    else:
        print("no")
else:
    for i in range(n-1):
        if i%2==0 and arr[i]>arr[i+1]:
            c+=1
        if i%2!=0 and arr[i]<arr[i+1]:
            c+=1
    if c==n-1:
        print("yes")
    else:
        print("no")
    
    