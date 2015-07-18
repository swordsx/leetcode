class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1: return s
        lines = [''] * numRows
        i = 0; j = 0
        while i < len(s):
            while j < numRows - 1 and i < len(s):
                lines[j] += s[i]
                i += 1; j += 1
            while j > 0 and i < len(s):
                lines[j] += s[i]
                i += 1; j -= 1
        return ''.join(lines)
