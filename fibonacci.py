n=int(input())
a=0
b=1
for i in range(0,n):
    print("%d"%a,end=' ')
    c=a+b
    a=b
    b=c