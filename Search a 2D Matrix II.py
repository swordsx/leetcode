class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if target > matrix[i][-1] or target < matrix[i][0]: continue
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) / 2
                if matrix[i][mid] == target: return True
                elif matrix[i][mid] > target: high = mid - 1
                else: low = mid + 1
        return False


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        def search(rowS, colS, rowE, colE):
            if rowS == rowE and colS == colE:
                return target == matrix[rowS][colS]
            if rowS > rowE or colS > colE:
                return False
            if matrix[rowS][colS] > target or matrix[rowE][colE] < target:
                return False
            rowM = (rowS + rowE) / 2
            colM = (colS + colE) / 2
            return search(rowS, colS, rowM, colM) or \
                   search(rowS, colM + 1, rowM, colE) or \
                   search(rowM + 1, colS, rowE, colM) or \
                   search(rowM + 1, colM + 1, rowE, colE)

        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        return search(0, 0, m - 1, n - 1)
