class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def match(self, s, target, wordlen):
        i = 0
        cnt = collections.defaultdict(int)
        while i < len(s):
            curword = s[i : i + wordlen]
            cnt[curword] += 1
            if curword not in target or target[curword] < cnt[curword]:
                return False
            i += wordlen
        return True
        
    def findSubstring(self, s, words):
        target = collections.defaultdict(int)
        for word in words:
            target[word] += 1
        wordlen = len(words[0])
        substrlen = len(words) * wordlen
        result = []
        for i in range(len(s) - substrlen + 1):
            if self.match(s[i:i+substrlen], target, wordlen):
                result.append(i)
        return result
