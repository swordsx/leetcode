class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
        
class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result        
