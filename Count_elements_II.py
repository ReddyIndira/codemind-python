a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=0
l=0
d=[]
for i in arr:
    if i not in brr and i not in d:
        d.append(i)
        c+=1
for i in brr:
    if i not in arr and i not in d:
        d.append(i)
        l+=1
print(c+l)