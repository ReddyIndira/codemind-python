a=input()
c=0
d=0
o=0
for i in range(len(a)):
    if(a[i]=="L"):
        c+=1
    if(a[i]=="R"):
        d+=1
    if(c==d):
        o+=1
print(o)
        