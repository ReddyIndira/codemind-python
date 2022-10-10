n=int(input())
a=list(map(int,input().split()))
o=int(input())
b=list(map(int,input().split()))
t=[]
for i in range(n):
    t.insert(b[i],a[i])
for i in range(n):
    print(t[i],end=' ')