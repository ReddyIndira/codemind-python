a=input().lower()
b=input().lower()
l=list(set(a)&set(b))
s=''
c=0
for i in l:
    if i==" ":
        continue
    s+=i
    c=1
x=sorted(s)
if(c==0):
    print("-1")
else:
    for i in x:
        print(i,end="")



    
