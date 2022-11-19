# Given an array Arr[] of N integers. 
# Find the contiguous sub-array(containing at least one number) 
# which has the maximum sum and return its sum.



import math

def maxSubArraySum(self,arr,N):
        ##Your code here
        maxx = -math.inf - 1
        cur = 0
        for i in range(0,N):
            cur+= arr[i]
            if(cur>maxx):
                maxx = cur
            if (cur<0):
                cur = 0
                
        return maxx