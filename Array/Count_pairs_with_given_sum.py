t=int(input())
while(t>0):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        for x in range(i+1,n):
            if((arr[i]+arr[x])==k):
                count+=1
    
    print(count)
    t-=1