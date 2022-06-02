n=int(input())
def is_prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return True
    else:
        return False
s=0
p=0
q=0
for i in range(1,n):
    for j in range(1,n):
        if((is_prime(i) and is_prime(j)) and i!=j):
            if(j*i==n):
                s=1
                p=i
                q=j
                break
if(s==1):
    print(q,p)
if(s==0):
    print("-1")