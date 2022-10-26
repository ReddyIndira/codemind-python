a,b=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
c=0
d=[]
for i in arr:
    if i in brr and i not in d:
        d.append(i)
        c+=1
print(c)