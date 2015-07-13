class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        resLow, resHigh = -1, -1
        if not nums: return [resLow, resHigh]
        low, high = 0, len(nums) - 1
        while low < high - 1:
            mid = (low + high) / 2
            if nums[mid] == target: high = mid
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1
        if nums[high] == target: resLow = high
        if nums[low] == target: resLow = low

        low, high = 0, len(nums) - 1
        while low < high - 1:
            mid = (low + high) / 2
            if nums[mid] == target: low = mid
            elif nums[mid] < target: low = mid + 1
            else: high = mid - 1
        if nums[low] == target: resHigh = low
        if nums[high] == target: resHigh = high
        return [resLow, resHigh]
