class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        dp = [0x7FFFFFFFF] * (len(dungeon[0]) - 1) + [1]
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[i]) - 1, -1, -1):
                MIN = min(dp[j:j+2]) if j <= len(dungeon[i]) else dp[j]
                if dungeon[i][j] >= 0 and MIN <= dungeon[i][j]: dp[j] = 1
                else: dp[j] = MIN - dungeon[i][j]
        return dp[0]
