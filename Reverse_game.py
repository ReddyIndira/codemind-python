def rev(i):
    rev=0
    while i:
        d=i%10
        rev=rev*10+d
        i=i//10
    return rev
n=int(input())
a=list(map(int,input().split()))
for i in a:
    print(rev(i),end=" ")