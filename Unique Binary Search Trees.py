class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append(0)
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]
