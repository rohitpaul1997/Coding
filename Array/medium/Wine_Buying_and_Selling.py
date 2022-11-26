# Given an array, arr[] of size N represents N house built along a straight line with equal distance between adjacent houses.
#  Each house has a certain number of wine and they want to buy/sell those wines to other houses.
#  Transporting one bottle of wine from one house to an adjacent house results in one unit of work.
#  The task is to find the minimum number of work is required to fulfill all the demands of those N houses.

# if a[i] < 0, then ith house wants to sell a[i] number of a wine bottle to other houses.
# if a[i] > 0, then ith house wants to buy a[i] number of a wine bottle from other houses.
# Note: One have to print the minimum number such that, all the house can buy/sell wine to each other.
# It is guaranteed that sum of all the elements of the array will be 0.

# Example 1:

# Input: N = 5, arr[] = {5, -4, 1, -3, 1}
# Output: 9
# Explanation:
# 1th house can sell 4 wine bottle to 0th house,
# total work needed 4*(1-0) = 4, new arr[] = 1,0,1,-3,1
# now 3rd house can sell wine to 0th, 2th and 4th.
# so total work needed = 1*(3-0)+1*(3-2)+1*(4-3) = 5
# So total work will be 4+5 = 9


def wineSelling(self, A, N):
    # code here
    # 		ans = 0
    # 		sum = 0
    # 		for i in range(N):
    # 		    ans += abs(sum)
    # 		    sum += A[i]
    # 		return ans

    buy = []
    sell = []
    for i in range(N):
        if(A[i] > 0):
            buy.append([A[i], i])
        else:
            sell.append([A[i], i])

    ans, i, j, dis = 0, 0, 0, 0
    while(i < len(buy) and j < len(sell)):

        mn = min(buy[i][0], abs(sell[j][0]))

        buy[i][0] -= mn

        sell[j][0] += mn

        dis = abs(buy[i][1]-sell[j][1])

        ans += (dis*mn)

        if(buy[i][0] == 0):

            i += 1

        if(sell[j][0] == 0):

            j += 1
