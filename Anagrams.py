class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        result = []
        anagramsDict = collections.defaultdict(list)
        for string in strs:
            letterCntDict = collections.defaultdict(int)
            for ch in string:
                letterCntDict[ch] += 1
            key = ''
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in letterCntDict:
                    key += ch + str(letterCntDict[ch])
            anagramsDict[key].append(string)
        for key in anagramsDict:
            if len(anagramsDict[key]) > 1:
                result += anagramsDict[key]
        return result


class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        result = []
        anagramsDict = collections.defaultdict(list)
        for string in strs:
            anagramsDict[''.join(sorted(string))].append(string)
        for key in anagramsDict:
            if len(anagramsDict[key]) > 1:
                result += anagramsDict[key]
        return result
