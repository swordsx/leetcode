import itertools
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        list = []
        for item in itertools.permutations(nums):
            list.append([i for i in item])
        return list
