class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        dp = [0] + [0x7FFFFFFF] * (len(triangle))
        for line in triangle:
            for i in range(len(line) - 1, -1, -1):
                dp[i] = min(dp[i], dp[i - 1]) + line[i]
        return min(dp)
