class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            #print 'fuck', low, mid, high
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]: high = mid - 1
                else: low = mid + 1
            else:
                if nums[mid] < target and target <= nums[high]: low = mid + 1
                else: high = mid - 1
        return -1
