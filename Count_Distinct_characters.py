s=input().lower()
t=[]
c=0
for i in s:
    if i not in t and i!=" ":
        t.append(i)
        c+=1
print(c)