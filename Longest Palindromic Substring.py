class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        maxLen = 0
        result = ''
        lens = len(s)
        for i in range(lens):
            offset = 1
            curMaxLen = 1
            while i - offset >= 0 and i + offset < lens and s[i + offset] == s[i - offset]:
                offset += 1
                curMaxLen += 2
            if curMaxLen > maxLen:
                maxLen = curMaxLen
                result = s[(i - offset + 1) : (i + offset)]
                
            offset = 0
            curMaxLen = 0
            while i - offset >= 0 and i + 1 + offset < lens and s[i - offset] == s[i + 1 + offset]:
                offset += 1
                curMaxLen += 2
            if curMaxLen > maxLen:
                maxLen = curMaxLen
                result = s[(i - offset + 1) : (i + offset + 1)]
        return result
