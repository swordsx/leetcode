class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        lenNums = len(nums)
        steps = [0] + [0x7FFFFFFF] * (lenNums - 1)
        for i in range(lenNums):
            j = min(lenNums - 1, i + nums[i])
            while steps[i] + 1 < steps[j]:
                steps[j] = steps[i] + 1
                j -= 1
        return steps[-1]
