class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []
        try:
            while True:
                result += matrix.pop(0)
                for i in range(len(matrix)):
                    result.append(matrix[i].pop())
                result += matrix.pop()[::-1]
                for i in range(len(matrix) - 1, -1, -1):
                    result.append(matrix[i].pop(0))
        except:
            pass
            
        return result
