from itertools import combinations
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        fullSet = [i + 1 for i in range(n)]
        for item in combinations(fullSet, k):
            res.append(item)
        return res
