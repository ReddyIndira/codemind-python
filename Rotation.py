T=int(input())
while(T):
    T-=1
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    while(b):
        b-=1
        t=l[a-1]
        del(l[a-1])
        f=l
        f.insert(0,t)
        l=f
    print(*l)
    