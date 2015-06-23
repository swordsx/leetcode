class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 2: return len(nums)
        slow = 2
        for fast in range(slow, len(nums)):
            if nums[fast] >= nums[slow] and nums[fast] != nums[slow - 2]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return slow
