class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        result = 0; num = 0; sign = 1; val = 0
        stack = []
        for ch in s:
            if ch == ' ': continue
            elif ch == '(':
                stack.append((val, sign))
                val = 0; sign = 1
            elif ch == '+' or ch == '-' or ch == ')':
                val += num * sign
                num = 0
                if ch == '+': sign = 1
                elif ch == '-': sign = -1
                else:
                    #FS: FromStack
                    (valFS, signFS) = stack.pop()
                    val = valFS + signFS * val
            else:
                num = num * 10 + int(ch)
        return val + num * sign
