class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1]) if words else 0
