class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = []
        for i in range(rowIndex + 1):
            result.append(1)
            for j in range(i - 1, 0, -1):
                result[j] += result[j - 1]
        return result
