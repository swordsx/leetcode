class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result.append([1])
            if i == 0: continue
            for j in range(i - 1):
                result[i].append(result[i - 1][j] + result[i - 1][j + 1])
            result[i].append(1)
        return result
    
