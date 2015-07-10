class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if stack and stack[-1] == dict[ch]:
                    stack.pop()
                else: return False
        return not stack
