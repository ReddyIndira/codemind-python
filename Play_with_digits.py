n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    while i:
        d=i%10
        s=s+d
        i=i//10
print(s)
        
    