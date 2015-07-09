class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        low, high = 0, len(nums) - 1
        nums.append(-0x7FFFFFFFF)
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] > nums[mid + 1] and nums[mid - 1] < nums[mid]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
        
