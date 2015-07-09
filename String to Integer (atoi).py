class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        INT_MAX = 0x7FFFFFFF
        INT_MIN = -1 - INT_MAX
        sign, result = 1, 0
        str = str.strip()
        if not str: return 0
        i = 0
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-': sign = -1
            i += 1
        while i < len(str):
            if str[i].isdigit():
                result = result * 10 + int(str[i])
            else:
                break
            i += 1
        result *= sign
        return max(min(result, INT_MAX), INT_MIN)
