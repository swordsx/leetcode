class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        val = int(str(abs(x))[::-1])
        if val > 0x7FFFFFFF: val = 0
        return sign * val
