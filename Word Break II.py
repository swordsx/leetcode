import collections
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreakI(self, s, wordDict):
        dpBackward = [False] * len(s) + [True]
        maxLen = 0
        for word in wordDict: maxLen = max(maxLen, len(word))
        for i in range(len(s) - 1, -1, -1):
            if dpBackward[i + 1] == False: continue
            for j in range(i, max(i - maxLen, -1), -1):
                if s[j:i+1] in wordDict:
                    dpBackward[j] = True
        return dpBackward
    def wordBreak(self, s, wordDict):
        maxLen = 0
        for word in wordDict: maxLen = max(maxLen, len(word))
        dpBackward = self.wordBreakI(s, wordDict)
        dpForward = [False] * len(s) + [True]
        splitIndices = collections.defaultdict(list)
        splitIndices[-1] = [[-1]]
        for i in range(len(s)):
            if dpForward[i - 1] is False or dpBackward[i] is False: continue
            for j in range(i, min(len(s), i + maxLen)):
                if s[i:j + 1] in wordDict:
                    dpForward[j] = True
                    for splitIndex in splitIndices[i - 1]:
                        splitIndices[j].append(splitIndex + [j])
        results = []
        for splitIndex in splitIndices[len(s) - 1]:
            result = []
            for i in range(1, len(splitIndex)):
                result.append(s[splitIndex[i-1]+1:splitIndex[i]+1])
            results.append(' '.join(result))
        return results
