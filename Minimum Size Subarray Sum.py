class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        slow, fast = 0, 0
        result, curSum = 0x7FFFFFFF, 0
        length = len(nums)
        while fast < length:
            while fast < length and curSum < s:
                curSum += nums[fast]
                fast += 1
            while curSum >= s:
                curSum -= nums[slow]
                slow += 1
            if slow:
                result = min(result, fast - slow + 1)
        return result if result != 0x7FFFFFFF else 0
