class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        if s == s[::-1]: return 0
        lens = len(s)
        for i in range(1, lens):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        isPal = [[False] * (i + 1) for i in range(lens)]
        dp = range(lens) + [-1]
        for i in range(lens):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or isPal[i - 1][j + 1]):
                    isPal[i][j] = True
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        return dp[lens - 1]
        
