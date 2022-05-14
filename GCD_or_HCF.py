a,b=map(int,input().split())
c=a
if a>b:
    a,b=b,a
while True:
    if (a%c==0 and b%c==0):
        print(c)
        break
    c-=1
    
    