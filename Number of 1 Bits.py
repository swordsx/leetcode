class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        for i in range(32):
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count
