class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0: return False
        while n:
            if n & 1 == 1:
                return n >> 1 == 0
            n >>= 1
            
#################
            
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0
