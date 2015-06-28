class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        result = 0
        while n:
            result += n / 5
            n /= 5
        return result
