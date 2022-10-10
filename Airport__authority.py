n=int(input())
b=[]
c=0
for i in range(1,n+1):
    T=int(input())
    b.append(T)
x=int(input())
for i in b:
    if(i<=x):
        c+=1
    else:
        c+=2
print(c)
