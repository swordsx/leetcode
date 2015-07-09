class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        dp = [False] * len(s) + [True]
        for i in range(len(s)):
            if dp[i - 1] is False: continue
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    dp[j] = True
        return dp[len(s) - 1]
