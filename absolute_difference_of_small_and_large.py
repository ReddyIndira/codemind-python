
    
    
    
s=input().split()
d=[]
for i in s:
    l=min(i)
    m=max(i)
    d.append(abs(ord(l)-ord(m)))
for i in d:
    print(i,end=' ')
    