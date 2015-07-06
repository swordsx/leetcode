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


class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        ss = '$#' + '#'.join([ch for ch in s]) + '#%'
        ID, mx, lenss = 1, 1, len(ss)
        p = [1] * lenss
        maxi = 0
        
        for i in range(1, lenss - 1):
            if mx > i:
                p[i] = min(p[ID * 2 - i], mx - i)
            while ss[i + p[i]] == ss[i - p[i]]:               
                p[i] += 1
            if p[i] + i > mx:
                ID, mx = i, p[i] + i
            if p[i] > p[maxi]:
                maxi = i
        result = ss[maxi-p[maxi]+1:maxi+p[maxi]]
        return ''.join(result.split('#'))
