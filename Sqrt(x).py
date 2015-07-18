class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x <= 1: return x
        low, high = 0, min(x, 65536)
        while low < high - 1:
            mid = (low + high) / 2
            square = mid * mid
            if square == x: return mid
            elif square < x: low = mid
            else: high = mid
        return low
