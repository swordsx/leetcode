import itertools
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) + 1):
            for item in itertools.combinations(nums, i):
                result.append(list(item))
        return result
        
  class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        result = []
        lenNums = len(nums)
        for i in range(2 ** lenNums):
            item = []
            for bit in range(lenNums):
                if i & (1 << bit):
                    item.append(nums[bit])
            result.append(item)
        return result
