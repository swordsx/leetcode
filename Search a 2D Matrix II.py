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
