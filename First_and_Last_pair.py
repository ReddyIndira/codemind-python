n=int(input())
a=list(map(int,input().split()))
b=[]
i=0
while i!=n//2:
    b.append(a[i])
    b.append(a[(n-1)-i])
    i+=1
if len(a)%2!=0:
    b.append(a[i])
    b.append(0)
print(*b)