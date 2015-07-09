class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) / 2
            elem = matrix[mid / n][mid % n]
            if elem == target:
                return True
            elif elem < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
