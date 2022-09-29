
    
    
  
s=input()
t=list()
d=0
for i in s:
    if i not in t:
        t.append(i)
for i in t:
    count=0
    for j in range(0,len(s)):
        if s[j]==i:
            count+=1
    if count%2!=0:
        d+=1
if d<2:
    print('Valid String')
else:
    print('Not Valid')  
    
    
    
    
    
    
    
    
    
    
    
    
    