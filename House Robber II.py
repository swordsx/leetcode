class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums: return 0
        length = len(nums)
        if length <= 3: return max(nums)
        dp1 = [0] * length
        dp2 = [0] * length
        dp1[0] = nums[0]
        dp1[1] = max(nums[1], dp1[0])
        dp2[1] = nums[1]
        for i in range(2, length):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[length - 2], dp2[length - 2],
                   dp2[length - 3] + nums[length - 1])
