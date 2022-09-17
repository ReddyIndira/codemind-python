s1=input().lower().split()
s2=input().lower().split()
c=[]
for i in s1:
    if i in s2:
        c.append(i)
for i in s2:
    if i in c:
        print(i,end=' ')
        
