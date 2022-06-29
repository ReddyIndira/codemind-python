n=int(input())
l=list(map(int,input().split()))
d=[]
s=0
for i in l:
    if i not in d and i%2==0:
        d.append(i)
        s+=1
print(s)