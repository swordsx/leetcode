class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        low = 0; high = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while low < high:
            mid = (low + high) / 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                return min(self.findMin(nums[:mid+1]), self.findMin(nums[mid+1:]))
        return nums[low]
