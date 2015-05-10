class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        def check(i, j):
            if board[i][j] == '.':
                return True
            for col in range(9):
                if j != col and board[i][col] == board[i][j]:
                    return False
            for row in range(9):
                if i != row and board[row][j] == board[i][j]:
                    return False
            for row in range(i / 3 * 3, i / 3 * 3 + 3):
                for col in range(j / 3 * 3, j / 3 * 3 + 3):
                    if i != row and j != col and board[row][col] == board[i][j]:
                        return False
            return True
        
        def solve(i, j):
            if i == 9:
                return True
            if board[i][j] == '.':
                for num in range(1, 10):
                    board[i][j] = str(num)
                    if check(i, j):
                        if solve(i + (j + 1) / 9, (j + 1) % 9):
                            return True
                board[i][j] = '.'
            else:
                return solve(i + (j + 1) / 9, (j + 1) % 9)
            return False

        solve(0, 0)
