a,b=map(int,input().split())
n=list(map(int,input().split()))
s=0
c=0
for i in range(a):
    s=0
    for j in range(i,a):
        s+=n[j]
        if(s>b):
            break
        if(s==b):
            c+=1
print(c)
    
        
        