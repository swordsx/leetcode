class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        for i in range(m): grid[i].append('0')
        grid.append(['0'] * n)
        visited = [[False] * n for i in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or visited[i][j]: continue
                queue = [(i, j)]
                visited[i][j] = True
                while queue:
                    iCur, jCur = queue.pop(0)
                    for (iOffset, jOffset) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        iNext, jNext = iCur + iOffset, jCur + jOffset
                        if grid[iNext][jNext] == '1' and visited[iNext][jNext] == False:
                            queue.append((iNext, jNext))
                            visited[iNext][jNext] = True
                result += 1
        return result
