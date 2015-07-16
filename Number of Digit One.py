class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        cnt = 0
        base = 1
        while base <= n:
           curDigit = (n / base) % 10
           cnt += n / base / 10 * base
           if curDigit > 1: cnt += base
           elif curDigit == 1: cnt += (n % base + 1) 
           base *= 10
        return cnt
