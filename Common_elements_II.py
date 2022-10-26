a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
d=[]
for i in arr:
    if i not in brr and i not in d:
        d.append(i)
for i in brr:
    if i not in arr and i not in d:
        d.append(i)
print(*d)