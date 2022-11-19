# Given an array of integers. Find the Inversion Count in the array. 

# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. 
# If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the 
# nversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

# Example 1:

# Input: N = 5, arr[] = {2, 4, 1, 3, 5}
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 
# has three inversions (2, 1), (4, 1), (4, 3).






def inversionCount(self, arr, n):
        result=self.merge_sort(arr,0,n-1)
        return result
def merge_sort(self,arr,left,right):
        result=0
        if(left<right):
            mid=(left+right)//2
            result+=self.merge_sort(arr,left,mid)
            result+=self.merge_sort(arr,mid+1,right)
            result+=self.merge(arr,left,mid,right)
        return result
def merge(self,arr,left,mid,right):
        l=arr[left:mid+1]
        r=arr[mid+1:right+1]
        i=0
        j=0
        k=left
        count=0
        n1=len(l)
        n2=len(r)
        while(i<len(l) and j<len(r)):
            if l[i]<=r[j]:
                arr[k]=l[i]
                k+=1
                i+=1
            else:
                arr[k]=r[j]
                j+=1
                k+=1
                count+=n1-i
        while(i<n1):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<n2):
            arr[k]=r[j]
            j+=1
            k+=1
        return count