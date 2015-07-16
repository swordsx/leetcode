class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0: return 1
        if x == 0 or x == 1: return x
        if x == -1: return x if n & 1 else -x

        if n < 0:
            x, n = 1 / x, -n
        result = 1
        while n:
            if n & 1: result *= x
            x *= x
            n >>= 1
        return result
