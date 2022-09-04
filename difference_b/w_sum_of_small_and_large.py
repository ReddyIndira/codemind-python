s1=input().lower().split()
d=[]
f=[]
s=0
k=0
for i in s1:
    l=min(i)
    d.append(l)
for i in s1:
    m=max(i)
    f.append(m)
for i in d:
    s=s+ord(i)
for i in f:
    k=k+ord(i)
print(abs(s-k))
    