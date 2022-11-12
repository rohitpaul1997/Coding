
def rotate(arr,n):
    temp=arr[n-1]
    for i in range (len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    return arr  



if __name__ =="__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        rotate(arr , n)
        print(arr)
        t-=1