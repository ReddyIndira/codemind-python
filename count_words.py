a=input().lower().split()
l="aeiou"
c=0
for i in a:
    if i[0] in l and i[len(i)-1] not in l:
        c+=1
print(c)