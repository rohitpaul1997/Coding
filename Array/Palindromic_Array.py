# Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. 
# Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

def palindrom(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False

def PalinArray(arr,n):
    for x in arr:
        if not palindrom(x):
            return False
    return True        




if __name__ == "__main__":
    t = int(input())
    while t>0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr,n):
            print(1)
        else: 
            print(0)

        t-=1       