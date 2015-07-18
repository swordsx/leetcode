class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        dpNeg = [num for num in nums]
        dpPos = [num for num in nums]
        for i in range(1, len(nums)):
            tup = (nums[i], nums[i] * dpNeg[i - 1], nums[i] * dpPos[i - 1])
            dpNeg[i] = min(tup)
            dpPos[i] = max(tup)
        return max(dpPos)
