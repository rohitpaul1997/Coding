# Given an array a[ ] of N elements. Consider array as a circular array i.e. element after an is a1. 
# The task is to find maximum sum of the absolute difference between consecutive elements with rearrangement of array
#  elements allowed i.e. after any rearrangement of array elements find |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1|.



def maxSum(arr,n):
    # code here
    arr.sort()
    i = 0
    j = len(arr)-1
    sum = 0
    while(i<j):
        sum+= abs(arr[i]-arr[j])+abs(arr[j]-arr[i+1])
        i+=1
        j-=1
    sum+=arr[int(n/2)]-arr[0]
    return sum
    