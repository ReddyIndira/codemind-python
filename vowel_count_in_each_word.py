a=list(map(str,input().split()))
s="aeiouAEIOU"
d=[]
for i in a:
    c=0
    for j in i:
        if j in s:
            c+=1
    d.append(c)
for i in d:
    print(i,end=' ')