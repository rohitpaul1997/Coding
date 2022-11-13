# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.




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