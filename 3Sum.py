class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        result = []
        nums.sort()
        lenNums = len(nums)
        for i in range(lenNums - 2):
            if i and nums[i] == nums[i - 1]: continue
            j, k = i + 1, lenNums - 1
            target = 0 - nums[i]
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]: j += 1; continue
                if k < lenNums - 1 and nums[k] == nums[k + 1]: k -= 1; continue
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1; k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return result
