# Given an array arr[] of N non-negative integers representing the height of blocks. 
# If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

# Example 1:

# Input:
# N = 6
# arr[] = {3,0,0,2,0,4}
# Output:
# 10

# Example 2:

# Input:
# N = 4
# arr[] = {7,4,0,9}
# Output:
# 10
# Explanation:
# Water trapped by above 
# block of height 4 is 3 units and above 
# block of height 0 is 7 units. So, the 
# total unit of water trapped is 10 units



def trappingWater(self, arr,n):
        #Code here
        left = 0
        right = n-1 
        l_max = 0
        r_max = 0
        result = 0
        while (left <= right):
            if r_max <= l_max:
                result += max(0, r_max-arr[right])
                r_max = max(r_max, arr[right])
                right -= 1
            else:
                result += max(0, l_max-arr[left])
                l_max = max(l_max, arr[left])
                left += 1
        return result