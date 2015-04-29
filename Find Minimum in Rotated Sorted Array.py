class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        low = 0; high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]