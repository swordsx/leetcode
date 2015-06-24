class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        i = 0
        while i < len(strs[0]):
            currentLetterIsInCommonPrefix = True
            currentLetter = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != currentLetter:
                    currentLetterIsInCommonPrefix = False
                    break
            if not currentLetterIsInCommonPrefix:
                break
            i += 1
        return strs[0][:i]
