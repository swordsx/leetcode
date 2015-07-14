class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        letters = []
        while n:
            n -= 1
            letters.append(chr(n % 26 + ord('A')))
            n /= 26
        return ''.join(letters[::-1])
