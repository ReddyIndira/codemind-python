n=input()
n=n.lower()
k=set(n)
k=list(k)
if(k.count(" ")>=1):
    j=k.index(" ")
    k.pop(j)
    print(len(k))
else:
    print(len(k))

  