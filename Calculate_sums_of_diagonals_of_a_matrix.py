n=int(input())
s=0
i=0
j=0
p=0
for i in range(0,n):
    a=list(map(int,input().split()))
    for j in range(0,n):
        if(i==j):
            s=s+a[j]
        if(i+j==n-1):
            p=p+a[j]
print("Principal Diagonal:",end="")
print(s)
print("Secondary Diagonal:",end="")
print(p)
            