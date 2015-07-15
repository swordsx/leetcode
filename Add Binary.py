class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if len(a) < len(b): return self.addBinary(b, a)
        result = [0] * (len(a) + 1)
        a, b = a[::-1], b[::-1]
        for i in range(len(b)):
            result[i] = int(a[i]) + int(b[i])
        for i in range(len(b), len(a)):
            result[i] = int(a[i])
        for i in range(len(a)):
            result[i + 1] += result[i] / 2
            result[i] %= 2

        if result[-1] == 0: result.pop()
        result = result[::-1]
        return ''.join(map(lambda digit: str(digit), [digit for digit in result]))
