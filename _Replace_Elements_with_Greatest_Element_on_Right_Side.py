n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    if(i==n-1):
        a[i]=-1
    else:
        c=0
        for j in range(i+1,len(a)):
            if(c<a[j]):
                c=a[j]
        a[i]=c
print(*a)