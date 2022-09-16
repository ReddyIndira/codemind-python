z=input()
g="aeiouAEIOU"
o=[]
for i in z:
    if i in g and not i in o:
        o.append(i)
print(*o)
    