s=input()
max=0
for i in range(0,len(s)):
    if s[i] in 'aeiou':
        c=1
        for j in range(i+1,(len(s))):
            if s[j] in 'aeiou':
                c+=1
            else:
                break
        if(c>max):
            max=c
print(max)

