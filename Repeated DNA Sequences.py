class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        _set = set()
        result = set()
        for i in range(len(s) - 9):
            sub = s[i : i + 10]
            if sub not in _set:
                _set.add(sub)
            else:
                result.add(sub)
        return list(result)
