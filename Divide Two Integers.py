class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        MAX_INT = 0x7FFFFFFF
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        product, quotient = 0, 0
        for i in range(31, -1, -1):
            if (product + (divisor << i)) <= dividend:
                product += (divisor << i)
                quotient += (1 << i)
        if sign == -1: quotient = 0 - quotient        
        return min(quotient, MAX_INT)
