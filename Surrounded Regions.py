class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board: return
        m, n = len(board), len(board[0])
        visited = [[False] * n for i in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    visited[i][j] = True
                    continue
                queue = [(i, j)]
                stack = []
                needModify = True
                while queue:
                    (icur, jcur) = queue.pop(0)
                    if icur < 0 or jcur < 0 or icur == m or jcur == n:
                        needModify = False
                    elif (not visited[icur][jcur]) and board[icur][jcur] == 'O':
                        stack.append((icur, jcur))
                        for direction in directions:
                            queue.append((icur + direction[0], jcur + direction[1]))
                        visited[icur][jcur] = True
                if needModify:
                    while stack:
                        (icur, jcur) = stack.pop()
                        board[icur][jcur] = 'X'
