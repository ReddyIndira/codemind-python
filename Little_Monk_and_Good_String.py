s=input()
vowels="aeiou"
max=0
c=0
for i in range(len(s)):
    if s[i] in vowels:
        c+=1
    else:
        if(max<c):
            max=c
        c=0
if(max<c):
    max=c
print(max)




