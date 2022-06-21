n=int(input())
dc=0
temp=n
while(temp!=0):
    dc+=1
    temp=temp//10
number=n
sum=0
while n!=0:
    sum+=(n%10)**dc
    n=n//10
    dc-=1
if(sum==number):
    print("True")
else:
    print("False")




