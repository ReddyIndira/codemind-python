s=input()
v="aeiouAEIOU"
o=[]
for i in s:
    if i in v:
        o.append(i)
i=len(o)-1
d=""
for j in s:
    if j in v:
        d+=o[i]
        i-=1
    else:
        d+=j
print(d)
        
        