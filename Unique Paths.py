class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dict = {}
        for i in range(m):
            for j in range(n):
                if i is 0 or j is 0:
                    dict[(i, j)] = 1
                else:
                    dict[(i, j)] = dict[(i - 1, j)] + dict[(i, j - 1)]
        return dict[(m - 1, n - 1)]
