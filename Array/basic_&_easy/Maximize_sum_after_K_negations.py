# Given an array of integers of size N and a number K., 
# Your must modify array arr[] exactly K number of times. 
# Here modify array means in each operation you can replace any array element either 
# arr[i] by -arr[i] or -arr[i] by arr[i]. You need to perform this operation in such a way that after K operations, 
# the sum of the array must be maximum.


def maximizeSum(self, arr, n, k):
        # Your code goes here
        arr.sort()
        i = 0
        j = 0
        while(i<k and arr[j]<0 and j<n-1):
            arr[j] = -(arr[j])
            j+=1
            i+=1
        while(i<k):
            arr[j] = -(arr[j])
            i+=1

        #print(arr)
        return sum(arr)