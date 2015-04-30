class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        dict = {}
        cur = n
        while cur not in dict:
            dict[cur] = True
            digits = cur % 10; sum = 0
            while cur:
                sum += (cur % 10) * (cur % 10)
                cur /= 10
            if sum == 1:
                return True
            cur = sum
        return False
