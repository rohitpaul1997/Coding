# You are given an array Arr of size N containing non-negative integers.
# Your task is to choose the minimum number of elements such that their sum should be greater
# than the sum of the rest of the elements of the array.


def minSubset(self, A, N):
    s = sum(A)
    A.sort()
    A.reverse()
    res = 0
    for i in range(N):
        res += A[i]
        s -= A[i]
        if res > s:
            return i+1
    return N
