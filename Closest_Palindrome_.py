def rev(n):
    temp=n
    rev=0
    while(temp>0):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    return rev
n=int(input())
for i in range(n-1,0,-1):
    if(i==rev(i)):
        y=i
        break
i=n+1
while(i>0):
    if(i==rev(i)):
        z=i
        break
    else:
        i+=1
if(abs(n-z)>abs(n-y)):
    print(y)
if(abs(n-y)==abs(n-z)):
    print(y,z)
if(abs(n-y)>abs(n-z)):
    print(z)
    