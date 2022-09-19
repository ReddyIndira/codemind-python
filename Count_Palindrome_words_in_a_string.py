s=input().lower().split()
c=[]
for i in s:
    if(i==i[::-1]):
        c.append(i)
print(len(c))