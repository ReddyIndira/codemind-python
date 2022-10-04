n=int(input())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
s1=0
s2=0
for i in arr:
    s1=s1+i
for j in brr:
    s2=s2+j
if(s2>s1):
    print(s2-s1)
else:
    print("0")
    
