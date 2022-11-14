
def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        i=0
        j=0
        summ=0
        smallest=float('inf')
        while(i<n):
            summ+=a[i]
            while(j<=i and summ-a[j]>x):
                summ-=a[j]
                j+=1
            if(summ>x):
                smallest=min(smallest,i-j+1)
            i+=1
        if(smallest==float('inf')):
            return 0
        return smallest


# Driver program
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
print("Not possible") if (res1 == n1 + 1) else print(res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x)
print("Not possible") if (res2 == n2 + 1) else print(res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
print("Not possible") if (res3 == n3 + 1) else print(res3)