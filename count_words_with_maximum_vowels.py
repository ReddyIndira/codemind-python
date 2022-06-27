l=list(map(str,input().split()))
c=0
d=[]
for i in l:
    c=0
    for j in i:
        if j in "aeiouAEIOU":
            c=c+1
    d.append(c)
dup=[]
for i in d:
    if(i==max(d)):
        dup.append(i)
print(len(dup))

            
            