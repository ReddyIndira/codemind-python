s=input()
c=0
d=0
for i in s:
    if(i=="z"):
        c+=1
    if(i=='o'):
        d+=1
if(d==2*c):
    print("Yes")
else:
    print("No")