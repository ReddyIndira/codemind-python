a,b=map(int,input().split())
a=str(a)
i=int(a[:b])
r=int(a[-b:])
print(abs(i-r))


