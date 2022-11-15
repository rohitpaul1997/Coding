# Given an array arr[] of size N and an element k. The task is to find all elements in array that appear more than n/k times.


def countOccurence(self,arr,n,k):
        #Your code here
        k = n//k
        dic = {}
        
        for ele in arr:
            if ele in dic:
                dic[ele]+=1
            else:
                dic[ele]=1
                
        count = 0
        for key in dic:
            if dic[key] > k:
                count+=1
                
        return count 