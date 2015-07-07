class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        headRow, headCol = [False] * m, [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    headRow[i] = headCol[j] = True
        for i in range(m):
            if headRow[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if headCol[j]:
                for i in range(m):
                    matrix[i][j] = 0
