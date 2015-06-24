class Solution:
    # @param {integer} n
    # @return {string[][]}
    def check(self, pos):
        for i in range(pos):
            if self.board[pos] == self.board[i] or abs(self.board[pos] - self.board[i]) == pos - i: return False
        return True

    def attempt(self, pos, n):
        if pos == n:
            result = []
            for i in range(n):
                line = '.' * (self.board[i]) + 'Q' + '.' * (n - self.board[i] - 1)
                result.append(line)
            self.results.append(result)
        else:
            for i in range(n):
                self.board[pos] = i
                if self.check(pos):
                    self.attempt(pos + 1, n)
    
    def solveNQueens(self, n):
        self.results = []
        self.board = [-1] * n
        self.attempt(0, n)
        return self.results
