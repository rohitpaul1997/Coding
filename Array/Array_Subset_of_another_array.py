

def isSubset(arr1,arr2):
    for i in arr2:
        if i not in arr1:
            return False
        else:
            arr1.pop(arr1.index(i))
    return True            



if __name__ == "__main__":
    t = int(input())
    while t>0:
        arr1 = list(map(int,input().strip().split()))
        arr2 = list(map(int,input().strip().split()))
        if isSubset(arr1,arr2):
            print("yes")
        else:
            print("No")  
        t-=1      