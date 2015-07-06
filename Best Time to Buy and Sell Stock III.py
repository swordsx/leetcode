class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices: return 0
        minPrice, maxPrice, result = prices[0], prices[-1], 0
        left, right = [0] * len(prices), [0] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] < minPrice: minPrice = prices[i]
            left[i] = max(left[i - 1], prices[i] - minPrice)
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > maxPrice: maxPrice = prices[i]
            right[i] = max(right[i + 1], maxPrice - prices[i])
            if left[i] + right[i] > result: result = left[i] + right[i]
        return result
