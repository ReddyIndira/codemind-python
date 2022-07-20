a=input()
c=0
for i in range(0,len(a)):
    if(ord(a[i])!=32):
        c+=1
print(c)