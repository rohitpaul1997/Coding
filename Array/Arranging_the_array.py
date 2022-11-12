# You are given an array of size N. 
# Rearrange the given array in-place such that all the negative numbers occur before positive numbers.
# (Maintain the order of all -ve and +ve numbers as given in the original array).


def Rearrange( arr, n):
    # Your code goes here
    negative = []
    positive = []
    
    for i in range(n):
        if arr[i]< 0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])
    
    for i in range(len(negative)):
        arr[i] = negative[i]
    
    for i in range(len(positive)):
        arr[len(negative) + i] = positive[i]


if __name__=="__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Rearrange(arr,n)
        print(arr)
        t-=1       