class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        dp = [[1] * (len(s) + 1)]
        for i in range(len(t)):
            dp.append([0])
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i + 1].append(dp[i][j] + dp[i + 1][j])
                else:
                    dp[i + 1].append(dp[i + 1][j])
        return dp[len(t)][len(s)]
