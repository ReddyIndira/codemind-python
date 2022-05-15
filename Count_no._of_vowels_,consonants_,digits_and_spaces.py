n=(input())
v=0
d=0
w=0
c=0
i=0
while i<len(n):
    if(n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U' or  n[i]=='a' or n[i]=='e' or  n[i]=='i' or n[i]=='o'or n[i]=='u'):
        v+=1
    elif(n[i]>='0' and n[i]<='9'):
        d+=1
    elif(n[i]==' '):
        w+=1
    else:
        c+=1
    i+=1
print('Vowels: %d'%v)
print('Consonants: %d'%c)
print('Digits: %d'%d)
print('White spaces: %d'%w)

    
