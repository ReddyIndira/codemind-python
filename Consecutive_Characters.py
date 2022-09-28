n=input()
c=1
d=[]
max=0
for i in range(0,len(n)-1):
    if(n[i]==n[i+1]):
        c+=1
    else:
        if(c>max):
            max=c
        c=1
        continue
if(c>max):
    max=c
print(max)