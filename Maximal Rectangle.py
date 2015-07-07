class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        result = 0
        for i in range(len(height)):
            if stack and height[i] <= height[stack[-1]]:
                while stack and height[stack[-1]] > height[i]:
                    j = stack.pop()
                    result = max(result, height[j] * ((i - stack[-1] - 1) if stack else i))
            stack.append(i)
        return result

    def maximalRectangle(self, matrix):
        if not matrix: return 0
        for line in matrix: line.append('0')
        matrix.append(['0'] * len(matrix[0]))
        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i - 1][j] + 1
        result = 0
        for line in dp:
            result = max(result, self.largestRectangleArea(line))
        return result
