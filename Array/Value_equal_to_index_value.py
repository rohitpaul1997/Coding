

class Solution:

    def indexValue(self,arr,n):
        ans = []
        for i in range(n):
            if i+1 == arr[i]:
                ans.append(arr[i])

        return ans        



if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        ans = ob.indexValue(arr,n)
        if(len(ans)==0):
            print("Not Found")
        else:
            print(ans)
        t-=1                    


