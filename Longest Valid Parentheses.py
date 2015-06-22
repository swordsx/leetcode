class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        result = 0
        available = 0
        dp = [0] * (len(s) + 1)
        for i in range(len(s)):
            if s[i] == '(':
                available += 1
            elif available > 0:
                available -= 1
                dp[i] = dp[i - 1] + 2
                dp[i] += dp[i - dp[i]]
                result = max(result, dp[i])
        return result
