n=int(input())
a=list(map(int,input().split()))
o=[]
for i in a:
    if i not in o:
        o.append(i)
for i in o:
    print(i,a.count(i),end=" ")