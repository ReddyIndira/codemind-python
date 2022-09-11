n=int(input())
arr=list(map(int,input().split()))
mid=n//2
for i in range(mid):
    print(arr[i],arr[mid+i],end=' ')
    
    