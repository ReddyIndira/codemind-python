a,b=list(map(int,input().split()))
h=list(map(int,input().split()))
m=list(map(int,input().split()))
l=set(h)
n=set(m)
c=0
for i in l:
    if i not in n:
        c+=1
for i in n:
    if i not in l:
        c+=1
print(c)