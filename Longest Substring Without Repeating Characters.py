import collections
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        p1 = 0; p2 = 0
        result = 0; curLen = 0
        cnts = collections.defaultdict(int)
        for p2 in range(len(s)):
            cnts[s[p2]] += 1
            curLen += 1
            while cnts[s[p2]] > 1:
                cnts[s[p1]] -= 1
                p1 += 1
                curLen -= 1
            result = max(curLen, result)
        return result
