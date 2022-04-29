num=int(input())
temp=num
sum=0
while(num):
    d=num%10;
    num=num//10;
    sum=sum+d;
if(temp%sum==0):
        print('True');
else:
        print('False');
    
    
    