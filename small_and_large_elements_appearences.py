s=list(map(str,input().split()))
d=[]
c=[]
for i in s:
    l=min(i)
    d.append(l)
    m=max(i)
    d.append(m)
    for j in i:
        c.append(j)
a=min(d)
b=max(d)
print(a,end=' ')
print(c.count(a),end=' ')
print(b,end=' ')
print(c.count(b),end=' ')

    