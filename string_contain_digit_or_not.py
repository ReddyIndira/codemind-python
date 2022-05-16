Astr=input()
c=0
for i in range(len(Astr)):
    if(Astr[i]>='0' and Astr[i]<='9'):
        c+=1
if(c==0):
    print("Doesn't contain digit")
else:
    print('Contains %d digit'%c)