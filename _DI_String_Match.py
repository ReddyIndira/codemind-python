s=input()
m=len(s)
l=0
for i in s:
    if(i=='I'):
        print(l,end=" ")
        l+=1
    if(i=='D'):
        print(m,end=" ")
        m-=1
print(m)
    