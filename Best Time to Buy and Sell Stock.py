class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        minPrice = 0x7FFFFFFF
        result = 0
        for price in prices:
            result = max(result, price - minPrice)
            minPrice = min(minPrice, price)
        return result
