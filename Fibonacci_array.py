n=int(input())
a=list(map(int,input().split()))
if (a[n-1]!=a[n-2]+a[n-3]):
    print("no")
else:
    for i in range(n-2):
        if(a[i]+a[i+1]!=a[i+2]):
            print("no")
            break
    else:
        print("yes")
    
