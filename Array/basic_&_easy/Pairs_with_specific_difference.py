# Given an array of integers, arr[] and a number, K.
# You can pair two numbers of the array if the difference between them is strictly less than K. 
# The task is to find the maximum possible sum of such disjoint pairs (i.e., each element of the array can be used at most once). 
# The Sum of P pairs is the sum of all 2P elements of pairs.

# Input  : 
# arr[] = {3, 5, 10, 15, 17, 12, 9}
# K = 4
# Output : 
# 62
# Explanation :
# Then disjoint pairs with difference less
# than K are, (3, 5), (10, 12), (15, 17)
# max sum which we can get is 
# 3 + 5 + 10 + 12 + 15 + 17 = 62
# Note that an alternate way to form 
# disjoint pairs is,(3, 5), (9, 12), (15, 17)
# but this pairing produces less sum.



def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here
        arr.sort(reverse=True)
        i=0
        c=0
        while i<N-1:
            if(arr[i]-arr[i+1])<K:
                c+=arr[i]+arr[i+1]
                i+=2
            else:
                i+=1
        return c 