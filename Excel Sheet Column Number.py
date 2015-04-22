class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        num = 0
        for c in s:
            num *= 26
            num += ord(c) - ord('A') + 1
        return num
