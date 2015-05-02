class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result = [([0] * n) for row in range(n)]
        row = 0; col = -1; direction = 'right'
        for i in range(1, n * n + 1):
            if direction == 'right':
                col += 1
                if col + 1 == n or result[row][col + 1] != 0:
                    direction = 'down'
            elif direction == 'down':
                row += 1
                if row + 1 == n or result[row + 1][col] != 0:
                    direction = 'left'
            elif direction == 'left':
                col -= 1
                if col - 1 == -1 or result[row][col - 1] != 0:
                    direction = 'up'
            else:
                row -= 1
                if row - 1 == -1 or result[row - 1][col] != 0:
                    direction = 'right'
            result[row][col] = i
        return result
