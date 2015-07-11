class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        m, n = len(p), len(s)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[-1][-1] = True
        for i in range(m):
            for j in range(n):
                if p[i] == '*':
                    dp[i][j] = (dp[i - 1][j] or dp[i - 2][j]) or ((p[i - 1] == '.' or p[i - 1] == s[j]) and dp[i][j - 1])
                    #dp[i - 1][j]例：s='a', p='a*'
                    #dp[i - 2][j]例：s='a', p='ab*'
                    #dp[i][j - 1]例：s='aa', p='a*'
                    #上述三例中，i, j对应m - 1, n - 1（换句话说，s, p为子串，非完整串）
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[i] == '.' or p[i] == s[j])
            dp[i][-1] = p[i] == '*' and dp[i - 2][-1]
            #例：s='aab', p='c*d*a*b'，则dp[5][-1] = dp[3][-1] = dp[1][-1] = True，也就是说，若当前子串偶数位全是*，可匹配s空子串
            #反例：s='aab', p='c*d*ea*b'，则dp[6][-1] = dp[4][-1] = False，'c*d*ea*'不能匹配s空子串
        return dp[m - 1][n - 1]
