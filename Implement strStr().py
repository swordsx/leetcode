class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        lenH, lenN = len(haystack), len(needle)
        for i in range(lenH - lenN + 1):
            if haystack[i:i+lenN] == needle:
                return i
        return -1
