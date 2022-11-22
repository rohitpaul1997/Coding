# Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

# Example 1:

# Input:
# N = 9, K = 3
# arr[] = 1 2 3 1 4 5 2 3 6
# Output: 
# 3 3 4 5 5 5 6 
# Explanation: 
# 1st contiguous subarray = {1 2 3} Max = 3
# 2nd contiguous subarray = {2 3 1} Max = 3
# 3rd contiguous subarray = {3 1 4} Max = 4
# 4th contiguous subarray = {1 4 5} Max = 5
# 5th contiguous subarray = {4 5 2} Max = 5
# 6th contiguous subarray = {5 2 3} Max = 5
# 7th contiguous subarray = {2 3 6} Max = 6



def max_of_subarrays(self,arr,n,k):
        # op = []
        # for i in range(n-k+1):
        #     op.append(max(arr[i:i+k]))
        # return op
        start = 0
        end = k-1
        
        queue = deque()
        ans = []
        i = 0
        
        
        while i < k:
            if len(queue) < 1:
                queue.append(i)
            elif arr[queue[-1]] > arr[i]:
                queue.append(i)
            elif arr[queue[-1]] <= arr[i]:
                while arr[queue[-1]] <= arr[i]:
                    queue.pop()
                    if len(queue) < 1:
                        queue.append(i)
                        break
                queue.append(i)
            i += 1
                
        ans.append(arr[queue[0]])
        
        while i < n:
            while len (queue) >= 1 and i - queue[0] > k - 1:
                queue.popleft()
            if len(queue) < 1:
                queue.append(i)
            elif arr[queue[-1]] > arr[i]:
                queue.append(i)
            elif arr[queue[-1]] <= arr[i]:
                while arr[queue[-1]] <= arr[i]:
                    queue.pop()
                    if len(queue) < 1:
                        break
                queue.append(i)
            
                
            ans.append(arr[queue[0]])
            i += 1
            
        return ans   