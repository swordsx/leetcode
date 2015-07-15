class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        length = len(s1)
        dp = [[[False] * (length - n) for i in range(length - n)] for n in range(length)]
        for i in range(length):
            for j in range(length):
                dp[0][i][j] = s1[i] == s2[j]

        for n in range(1, length):
            for i in range(length - n):
                for j in range(length - n):
                    for k in range(n):
                        dp[n][i][j] = ((dp[k][i][j] and dp[n-k-1][i+k+1][j+k+1]) or
                                       (dp[k][i][j+n-k] and dp[n-k-1][i+k+1][j]))
                        if dp[n][i][j]: break
        return dp[-1][0][0]
