# Given a array of N strings, find the longest common prefix among all strings present in the array.


def longestPrefix(arr):
    comp1 = min(arr)
    comp2 = max(arr)
    lcp = ""
    for i in range(len(comp1)):
        if comp1[i] != comp2[i]:
            break
        lcp += comp1[i]
        if lcp == "":
            return -1
    return lcp


if __name__ =="__main__":
    t = int(input())
    while t>0:
        arr = list(x for x in input().strip().split(" "))
        print(arr)
        print(longestPrefix(arr))
        t-=1

