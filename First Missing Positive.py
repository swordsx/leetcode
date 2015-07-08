class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            j = nums[i] - 1
            while j >= 0 and j < len(nums) and nums[j] != j + 1:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
