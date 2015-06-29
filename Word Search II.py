class Solution:

    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def search(self, i, j, string):
        if self.visited[i][j]: return
        self.visited[i][j] = True
        string += self.board[i][j]
        cur = self.trie
        startsWith = True
        for ch in string:
            if ch not in cur:
                startsWith = False
                break
            cur = cur[ch]
    
        if startsWith:
            if '$' in cur and string not in self.result:
                self.result.append(string)
            for x, y in self.offsets:
                self.search(i + x, j + y, string)
        self.visited[i][j] = False
            
    def findWords(self, board, words):
        self.board = board
        self.result = []
        self.trie = {}
        for word in words:
            cur = self.trie
            for ch in word:
                if ch not in cur: cur[ch] = {}
                cur = cur[ch]
            cur['$'] = '$'
        self.visited = [[False] * len(board[0]) + [True] for i in range(len(board))]
        self.visited.append([True] * (len(board[0]) + 1))
        self.offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        string = ''
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(i, j, string)
        return self.result
