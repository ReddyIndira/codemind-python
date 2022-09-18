def fun(i):
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    return c
s=input().lower().split()
o=[]
for i in s:
    p=fun(i)
    o.append(p)
print(o.count(max(o)))