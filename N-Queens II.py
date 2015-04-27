import itertools
class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        def check(item, n):
            for i in range(n):
                for j in range(i + 1, n):
                    if abs(item[i] - item[j]) == j - i:
                        return False
            return True
        count = 0
        for item in itertools.permutations(range(n)):
            if check(item, n):
                count += 1
        return count
