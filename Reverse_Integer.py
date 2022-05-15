n=int(input())
sum1=0
c=0
if n<1:
    n=n*-1
    c+=1

while(n):
    d=n%10
    sum1=sum1*10+d
    n=n//10
if c==1:
    print(-sum1)
else:
    print(sum1)