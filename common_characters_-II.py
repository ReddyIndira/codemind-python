s1=input().lower()
s2=input().lower()
c=[]
d=0
for i in s1:
    if i in s2 and i not in c and i!=" ":
        c.append(i)
        d+=1
print(d)
