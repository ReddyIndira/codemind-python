def pal(i):
    temp=i
    rev=0
    while i:
        d=i%10
        rev=rev*10+d
        i=i//10
    if(rev==temp):
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(pal(i)):
        c=c+1
print(c)