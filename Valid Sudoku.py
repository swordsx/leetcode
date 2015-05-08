class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        def check(board, i, j):
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
        for i in range(9):
            for j in range(9):
                if check(board, i, j) == False:
                    return False
        return True
