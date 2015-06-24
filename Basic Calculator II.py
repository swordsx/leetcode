class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        Sum = 0; sign = '+'; num = 0; product = 0; presign = '+'
        s += '+'
        for ch in s:
            if ch == ' ': continue
            elif ch in '+-*/':
                if ch in '+-':
                    if sign == '+': Sum += num
                    elif sign == '-': Sum -= num
                    else:
                        if sign == '*': product *= num
                        else: product /= num
                        if presign == '-': product *= -1
                        Sum += product
                elif ch in '*/':
                    if sign in '+-':
                        product = num
                        presign = sign
                    elif sign == '*': product *= num
                    else: product /= num
                sign = ch
                num = 0
            else:
                num = num * 10 + int(ch)
        return Sum
