class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid: return 0
        m = len(grid); n = len(grid[0])
        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[j + 1] = grid[i][j] + dp[j]
                elif j == 0:
                    dp[j + 1] = dp[j + 1] + grid[i][j]
                else:
                    dp[j + 1] = min(dp[j], dp[j + 1]) + grid[i][j]
        return dp[n]
