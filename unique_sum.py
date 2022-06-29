n=int(input())
l=list(map(int,input().split()))
d=[]
s=0
for i in l:
    if i not in d:
        d.append(i)
        s+=i
print(s)