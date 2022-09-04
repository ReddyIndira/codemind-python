s=input()
s=s.lower()
m="aeiou"
a=0
b=len(s)-1
c=0
while a<b:
    if s[a].isalpha() and s[b].isalpha():
        if (s[a] in m and s[b] not in m) or(s[a] not in m and s[b] in m):
            c+=1
    a+=1
    b-=1
print(c)
            
