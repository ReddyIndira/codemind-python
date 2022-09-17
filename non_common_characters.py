s1=input().lower()
s2=input().lower()
c=[]
for i in s1:
    if i not in s2 and i not in c and i!=" ":
        c.append(i)
for i in s2:
    if i not in s1 and i not in c and i!=" ":
        c.append(i)
c=sorted(c)
for i in c:
    print(i,end='')