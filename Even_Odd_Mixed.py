n=int(input())
d=0
dc=0
e=0
o=0
while(n!=0):
    d=n%10;
    n=n//10
    dc=dc+1
    if(d%2==0):
        e=e+1
    else:
        o=o+1
if(e==dc):
    print("Even")
elif(o==dc):
    print("Odd")
else:
    print("Mixed")
