a,b=list(map(int,input().split()))
h=list(map(int,input().split()))
m=list(map(int,input().split()))
c=[]
for i in h:
    if i in m:
        if i not in c:
            c.append(i)
print(*c)