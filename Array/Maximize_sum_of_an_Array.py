# Given an array A of N integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n 1.
# You are allowed to rearrange the elements of the array.
# Note: Since output could be large, hence module 109+7 and then print answer.

def maxSum(arr,n):
    arr.sort()
    sum = 0
    for index,value in enumerate(arr):
        sum += value*index
    return sum%1000000007    


if __name__ =="__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        sum = maxSum(arr,n)
        print(sum)
        t-=1