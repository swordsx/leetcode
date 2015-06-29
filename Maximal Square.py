class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        maxlen = 0
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen ** 2
