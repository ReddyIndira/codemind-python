def rev(n):
    rev=0
    while(n):
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev
n=int(input())
while(n):
    n+=rev(n)
    if(n==rev(n)):
        print(n)
        break