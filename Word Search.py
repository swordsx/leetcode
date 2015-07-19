class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        def search(i, j, k):
            if k == len(word) - 1 and board[i][j] == word[k]: return True
            visited[i][j] = True
            result = False
            if board[i][j] == word[k]:
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if visited[i + x][j + y] == False:
                        if search(i + x, j + y, k + 1):
                            result = True
                            break
            
            visited[i][j] = False
            return result

        if not board: return False
        m, n = len(board), len(board[0])
        visited = [[False] * n + [True] for i in range(m)] + [[True] * n]
        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True
        return False
