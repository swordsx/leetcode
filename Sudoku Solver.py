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

##################################


class Solution1:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    class Node:
        def __init__(self, row, col):
            self.row = row
            self.col = col
            self.u = None
            self.d = None
            self.l = None
            self.r = None
            
    def solveSudoku(self, board):
        matrix = self.exactCoverConstruct(board)
        self.linkMatrix(matrix)
        stack = []
        self.solveExactCover(matrix, stack)
        self.fillBoard(stack, matrix, board)
        
    def exactCoverConstruct(self, board):
        matrix = [[self.Node(0, i) for i in range(325)]]
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for candidate in range(1, 10):
                        rowMatrix = len(matrix)
                        matrix.append([self.Node(rowMatrix, 0) for i in range(4)])

                        matrix[rowMatrix][0].col = row * 9 + col + 1
                        matrix[rowMatrix][1].col = 81 + row * 9 + candidate
                        matrix[rowMatrix][2].col = 162 + col * 9 + candidate
                        matrix[rowMatrix][3].col = 243 + (row / 3 * 3 + col / 3) * 9 + candidate

                else:
                    num = int(board[row][col])
                    rowMatrix = len(matrix)
                    matrix.append([self.Node(rowMatrix, 0) for i in range(4)])
                    
                    matrix[rowMatrix][0].col = row * 9 + col + 1
                    matrix[rowMatrix][1].col = 81 + row * 9 + num
                    matrix[rowMatrix][2].col = 162 + col * 9 + num
                    matrix[rowMatrix][3].col = 243 + (row / 3 * 3 + col / 3) * 9 + num
        self.linkMatrix(matrix)
        return matrix
    
    def linkMatrix(self, matrix):
        for i in range(len(matrix[0])):
            matrix[0][i].u = matrix[0][i]
            matrix[0][i].d = matrix[0][i]
            matrix[0][i].l = matrix[0][i - 1]
            matrix[0][i].r = matrix[0][(i + 1) % len(matrix[0])]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j].l = matrix[i][j - 1]
                matrix[i][j].r = matrix[i][(j + 1) % len(matrix[i])]
                if i is 0:
                    matrix[i][j].u = matrix[i][j]
                    matrix[i][j].d = matrix[i][j]
                else:
                    col = matrix[i][j].col
                    matrix[i][j].u = matrix[0][col].u
                    matrix[i][j].d = matrix[0][col]
                    matrix[0][col].u.d = matrix[i][j]
                    matrix[0][col].u = matrix[i][j]
                    #header counter increase, used for split select
                    matrix[0][col].row += 1

    def deleteRow(self, matrix, node):
        for node in matrix[node.row]:
            if node.u.d is not node:
                continue
            node.u.d = node.d
            node.d.u = node.u
            matrix[0][node.col].row -= 1
            node = node.r
            
    def restoreRow(self, matrix, node):
        for node in matrix[node.row]:
            node.u.d = node
            node.d.u = node
            matrix[0][node.col].row += 1
            node = node.r
            
    def deleteCol(self, matrix, node):
        node = matrix[0][node.col]
        while node.l.r is node:
            node.l.r = node.r
            node.r.l = node.l
            node = node.d
            
    def restoreCol(self, matrix, node):
        node = matrix[0][node.col]
        while node.l.r is not node:
            node.l.r = node
            node.r.l = node
            node = node.d
            
    def selectCol(self, head):
        cur = head.r
        res = cur
        while cur is not head:
            if cur.row < res.row:
                res = cur
            cur = cur.r
        return res
        
    def solveExactCover(self, matrix, stack):
        head = matrix[0][0]
        if head.r is head:
            return True
        selectedCol = self.selectCol(head)
        if selectedCol.row == 0:
            return False
        cur = selectedCol.d
        while cur is not selectedCol:
            stack.append(cur.row)
            self.deleteRow(matrix, cur)
            stack1 = []
            for node in matrix[cur.row]:
                stack1.append(node)
                self.deleteCol(matrix, node)
                curr = matrix[0][node.col].d
                stack2 = []
                while curr is not matrix[0][node.col]:
                    stack2.append(curr)
                    self.deleteRow(matrix, curr)
                    curr = curr.d
                stack1.append(stack2)
                
            if self.solveExactCover(matrix, stack):
                return True
                
            while len(stack1):
                top = stack1.pop()
                if type(top) is list:
                    while len(top):
                        self.restoreRow(matrix, top.pop())
                else:
                    self.restoreCol(matrix, top)
            stack.pop()
            self.restoreRow(matrix, cur)
            
            cur = cur.d
        return False
        
    def fillBoard(self, stack, matrix, board):
        for rowMatrix in stack:
            num = (matrix[rowMatrix][1].col - 1) % 9 + 1
            row = (matrix[rowMatrix][1].col - 81 - num) / 9
            col = (matrix[rowMatrix][2].col - 162 - num) / 9
            board[row][col] = str(num)
            
