a=input()
s=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]==a[j] and i!=j):
            c+=1
    if(c==0):
        print(i)
        s=1
        break
if(s==0):
    print(-1)
