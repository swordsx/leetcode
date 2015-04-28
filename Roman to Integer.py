class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = dict[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if dict[s[i]] < dict[s[i + 1]]:
                num -= dict[s[i]]
            else:
                num += dict[s[i]]
        return num
