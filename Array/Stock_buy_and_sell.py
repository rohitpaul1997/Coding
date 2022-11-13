


def stockBuySell(arr,n):
    max=0
    min = arr[0]
    for i in range(n):
        if arr[i]<min:
            min = arr[i]
        elif (arr[i]-min)>max:
            max = arr[i]-min
    return max            




if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(stockBuySell(arr,n))
        t-=1