a=int(input())
while(a):
    b=int(input())
    s=list(map(int,input().split()))
    d=sorted(s)
    if d==s:
        print("0")
    else:
        print(max(d)-min(d))
a-=1
    
    