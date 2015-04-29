class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        list = [0]
        cur = 0
        for i in range((1 << n) - 1):
            for j in range(1 << n):
                mask = 1 << j
                if cur ^ mask not in list:
                    list.append(cur ^ mask)
                    cur = cur ^ mask
                    break
        return list
