class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        ss = '$#' + '#'.join([ch for ch in s]) + '#%'
        ID, mx, lenss = 1, 1, len(ss)
        p = [1] * ((lenss + 1) / 2)
        MPLFB = 0       #MaxPalindromeLengthFromBegin
        
        for i in range(1, (lenss + 1) / 2):
            if mx > i:
                p[i] = min(p[ID * 2 - i], mx - i)
            while ss[i + p[i]] == ss[i - p[i]]:               
                p[i] += 1
            if p[i] + i > mx:
                ID, mx = i, p[i] + i
            if p[i] == i:
                MPLFB = i - 1
        result = s[MPLFB:][::-1] + s
        return result
