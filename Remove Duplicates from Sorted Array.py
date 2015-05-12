class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] > nums[slow]:
                slow += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]
        return slow + 1
