class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0: return False
        digits = []
        while x:
            digits.append(x % 10)
            x /= 10
        return digits == digits[::-1]
