def prime(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        for i in range(2,int(n**0.5)+2):
            if n%i==0:
                return 1
        return 0
n=int(input())
if(prime(n)==1):
    print("not a prime")
else:
    print("prime")
