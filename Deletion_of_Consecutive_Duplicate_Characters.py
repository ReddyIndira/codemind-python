T=int(input())
for i in range(T):
    s=input()
    c=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c+=1
    print(c)