s1=input()
s2=input()
c=[]
for i in s1:
    for i in s2:
        if i in s1 and i in s2:
            c.append(i)
for i in c:
    if(len(s1)==len(s2)):
        print("True")
        break
    else:
        print("False")
        break
            