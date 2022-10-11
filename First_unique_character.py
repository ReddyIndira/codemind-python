s=input()
b=[]
c=0
for i in range(len(s)):
    if(s.count(s[i])==1):
        b.append(s[i])
        c+=1
        break
if(c==0):
    print("-1")
else:
    print(*b)

    
        
