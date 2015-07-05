class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums: return []
        curMin, curMax = nums[0], nums[0]
        nums.append(nums[-1] + 2)
        result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curMax = nums[i]
            else:
                if curMin == curMax:
                    result.append(str(curMax))
                else:
                    result.append(str(curMin) + '->' + str(curMax))
                curMin, curMax = nums[i], nums[i]
        return result
