def find(arr,n,x):
    ans = [-1,-1]
    for i in range(n):
        if arr[i] == x:
            if ans[0]==-1:
                ans[0]=i
            ans[1]=i
    return ans            

if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        x = int(input())
        ans = find(arr, n, x)
        print(*ans)
        t-=1