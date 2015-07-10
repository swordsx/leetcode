class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        mask = 0x7FFFFFFF
        while (m & mask) != (n & mask):
            mask <<= 1
        return m & mask
