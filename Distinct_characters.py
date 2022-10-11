s=input().lower()
t=[]
for i in s:
    if i not in t and i!=" ":
        t.append(i)
t=sorted(t)
for i in t:
    print(i,end="")
