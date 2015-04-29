class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ones = 0; twos = 0; threes = 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ~(ones & twos)
            ones &= threes
            twos &= threes
        return ones
