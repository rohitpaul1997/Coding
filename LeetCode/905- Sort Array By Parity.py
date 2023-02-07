def sortArrayByParity(nums: list[int]) -> list[int]:
    a = []
    for i in nums:
        if i % 2 == 0:
            a.insert(0, i)
            print(a)
        else:
            a.append(i)
            print(a)
    return a


print(sortArrayByParity([4,1,6,3,9,5]))