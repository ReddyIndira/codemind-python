s=input()
t=input()
ss=[]
tt=[]
for i in s:
    if(i=="#"):
        ss.pop()
    else:
        ss.append(i)
for i in t:
    if i=="#":
        tt.pop()
    else:
        tt.append(i)
if(ss==tt):
    print("True")
else:
    print("False")
        

        