def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    return 0
n=int(input())
for i in range(n,0,-1):
    if(prime(i)):
        a=i
        break
i=n+1
while(i>0):
    if(prime(i)):
        b=i
        break
    else:
        i+=1
x=abs(a-n)
y=abs(b-n)
if(x>y):
    print(y)
else:
    print(x)