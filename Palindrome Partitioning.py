class Solution:
    # @param {string} s
    # @return {string[][]}
    def isPalindrome(self, s):
        return s == s[::-1]

    def par(self, s, start):
        if start == len(s):
            self.result.append([substr for substr in self.stack])
        for end in range(start + 1, len(s) + 1):
            if self.isPalindrome(s[start:end]):
                self.stack.append(s[start:end])
                self.par(s, end)
                self.stack.pop()
    
    def partition(self, s):
        self.result = []
        self.stack = []
        self.par(s, 0)
        return self.result
