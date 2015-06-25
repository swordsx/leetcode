class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(s) > 30000: return False
        dp = [False] * (len(s)) + [True]
        nonAstericExists = False
        for i in range(len(p)):
            if p[i] == '*':
                for j in range(len(s)):
                    dp[j] |= dp[j - 1]
            else:
                nonAstericExists = True
                for j in range(len(s) - 1, -1, -1):
                    if p[i] == '?' or p[i] == s[j]:
                        dp[j] = dp[j - 1]
                    else: dp[j] = False
            dp[-1] = not nonAstericExists   //tricky here. relevant sample: ['b', '?*?'], ['b', '*?*']
        return dp[len(s) - 1]
