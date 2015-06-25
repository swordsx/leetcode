class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        dp = []
        for i in range(len(word1)):
            dp.append([0] * len(word2) + [i + 1])
        dp.append(range(1, len(word2) + 1) + [0])
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]: dp[i][j] = dp[i - 1][j - 1]
                else: dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[len(word1) - 1][len(word2) - 1]
