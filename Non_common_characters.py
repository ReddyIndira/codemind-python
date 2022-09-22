s1=list(input().lower().replace(' ',''))
s2=list(input().lower().replace(' ',''))
c=[]
for i in s1:
    if i not in s2 and i not in c:
        c.append(i)
for i in s2:
    if i not in s1 and i not in c:
        c.append(i)
print(len(c))
