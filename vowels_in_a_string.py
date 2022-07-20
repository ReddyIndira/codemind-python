a=input()
k=input()
v="aeiouAEIOU"
c=0
for i in a:
    if i in v:
        if(i==k):
            c+=1
            break
if(c!=0):
    print("True")
    print(a.index(i))
else:
    print("False")
            