class Solution:
    # @param {string} digits
    # @return {string[]}
    def product(self, digits, i, string):
        if i == len(digits):
            self.result.append(string)
            return
        for letter in self.dict[digits[i]]:
            self.product(digits, i + 1, string + letter)
    def letterCombinations(self, digits):
        if not digits: return []
        self.dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.result = []
        self.product(digits, 0, '')
        return self.result
        
————————————————————


class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        keys={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
            }
        possibleLetters = map(lambda s:list(keys.get(s)),digits)
        possibleCombinations = list(itertools.product(*possibleLetters))
        return list(map(''.join,possibleCombinations))
