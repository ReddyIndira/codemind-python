s=input().lower()
b=[]
for i in range(len(s)):
    if(s.count(s[i])==1) and s[i]!=" ":
        b.append(s[i])
c=sorted(b)
for i in c:
    print(i,end="")
    
