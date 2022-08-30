n = int(input())
a = list(map(int,input().split()))
b=[]
for i in range(len(a)):
    b.append(a[i])
if len(a)%2!=0:
    b.append(0)
print(*b)