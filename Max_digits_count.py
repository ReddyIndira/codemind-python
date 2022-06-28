def digit(n):
    c=0
    while(n>0):
        c+=1
        n//=10
    return c
n=int(input())
a=list(map(int,input().split()))
f=digit(max(a))
c=0
for i in a:
    if(digit(i)==f):
        c+=1
print(c)