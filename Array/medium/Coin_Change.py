# Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum,
# find the number of ways you can make sum by using different combinations from coins[ ].
# Note: Assume that you have an infinite supply of each type of coin.


# Example 1:

# Input:
# sum = 4 ,
# N = 3
# coins[] = {1,2,3}
# Output: 4
# Explanation: Four Possible ways are:
# {1,1,1,1},{1,1,2},{2,2},{1,3}.
# Example 2:

# Input:
# Sum = 10 ,
# N = 4
# coins[] ={2,5,3,6}
# Output: 5
# Explanation: Five Possible ways are:
# {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}
# and {5,5}.


def count(self, coins, N, Sum):
    # code here
    # if (sum == 0):
    #     return 1
    # if (sum < 0):
    #     return 0
    # if (sum < 0):
    #     return 0
    # if (n <= 0):
    #     return 0
    # return count(self,coins, n - 1, sum) + count(self,coins, n, sum-coins[n-1])

    dp = [0 for i in range(Sum+1)]
    dp[0] = 1
    for i in range(N):
        for j in range(coins[i], Sum+1):
            dp[j] += dp[j-coins[i]]
    return dp[Sum]
