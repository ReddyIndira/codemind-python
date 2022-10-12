s1=input().lower().split()
s2=input().lower().split()
b=[]
for i in s2:
    if i in s1 and i!=" ":
        b.append(i)
for i in b:
    print(i,end=" ")
        
