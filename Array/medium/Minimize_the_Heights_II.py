# Given an array arr[] denoting heights of N towers and a positive integer K.

# For each tower, you must perform exactly one of the following operations exactly once.

# Increase the height of the tower by K
# Decrease the height of the tower by K
# Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        maxo = arr[-1]
        mino = arr[0]
        out = maxo-mino
        for i in range(1, n):
            maxo = max(arr[i-1]+k, arr[-1]-k)
            mino = min(arr[i]-k, arr[0]+k)
            if mino < 0:
                continue
            out = min(out, maxo-mino)
        return out


        