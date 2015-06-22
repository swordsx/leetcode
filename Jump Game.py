class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            farthest = max(nums[i] + i, farthest)
            if farthest == i: break
        return farthest >= len(nums) - 1
