def fib(n):
    a=0
    b=1
    i=2
    print(a,b,end=' ')
    while(i<n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
        i+=1
n=int(input())
fib(n)