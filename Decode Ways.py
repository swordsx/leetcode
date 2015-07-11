class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s: return 0
        dp = [0] * len(s) + [1]
        for i in range(len(s)):
            if s[i] != '0':
                dp[i] = dp[i - 1]
            if i and s[i -1] != '0':
                n = int(s[i - 1]) * 10 + int(s[i])
                if n and n <= 26:
                    dp[i] += dp[i - 2]
        return dp[len(s) - 1]
