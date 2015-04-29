class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        dp = []
        for num in nums:
            if dp and dp[-1] > 0:
                dp.append(dp[-1] + num)
            else:
                dp.append(num)
        return max(dp)
