s=input()
c=[]
for i in s:
    c.append(s.count(i))
c=set(c)
p=c.remove(max(c))
for i in s:
     if s.count(i) in c:
         print(i,end="")
         break
if(len(c)==0):
    print(-1)