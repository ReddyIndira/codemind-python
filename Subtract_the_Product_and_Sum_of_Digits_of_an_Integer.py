
n=int(input())
i=1
sum=0
p=1
while(i<=n):
    r=n%10
    p=p*r
    sum=sum+r
    n=n//10
if(sum>=p):
        print(sum-p)
else:
        print(p-sum)
