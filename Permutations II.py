class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            nums.reverse()
        else:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = sorted(nums[i+1:])

    def permuteUnique(self, nums):
        nums.sort()
        origin = [num for num in nums]
        result = [nums]
        while True:
            self.nextPermutation(nums)
            if nums == origin:
                break
            result.append([num for num in nums])
        return result
