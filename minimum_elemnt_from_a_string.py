s=input().split()
a=s[len(s)-1]
k=min(a)
if k and k.lower() in a:
    print(k.lower())
else:
    print(k)