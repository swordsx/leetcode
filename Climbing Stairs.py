class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        dp = {0: 1, 1: 1}
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
