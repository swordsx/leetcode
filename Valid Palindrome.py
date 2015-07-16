class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i].isalnum() == False: i += 1
            elif s[j].isalnum() == False: j -= 1
            elif s[i].lower() == s[j].lower(): i, j = i + 1, j - 1
            else: return False
        return True
