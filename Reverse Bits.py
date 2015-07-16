class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result, mask1, mask2 = 0, 0x80000000, 1
        while mask1 >= 1:
            if mask2 & n: result += mask1
            mask1 >>= 1
            mask2 <<= 1
        return result
