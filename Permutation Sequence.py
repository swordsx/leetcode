class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        k -= 1
        digits = range(1, n + 1)
        queue = []
        factorials = [1] * (n + 1)
        for i in range(2, (n + 1)):
            factorials[i] = factorials[i - 1] * i
        while n:
            n -= 1
            queue.append(str(digits.pop(k / factorials[n])))
            k %= factorials[n]
        result = ''.join(queue)
        return result
