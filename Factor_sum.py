l=list(map(int,input().split(',')))
s=0
c=0
d=[]
for i in l:
    s=0
    for j in range(1,i+1):
        if(i%j==0):
            s=s+j
    if s in l:
        d.append(i)
        c+=1
if(c==0):
    print("-1")
else:
    d=sorted(d)
    print(*d)
        