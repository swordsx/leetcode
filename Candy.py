class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        cur = 1; result = 1; peakIndex = 0; peakVal = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                cur += 1
                peakIndex, peakVal = i, cur
            elif ratings[i] == ratings[i - 1]:
                cur = 1
                peakIndex, peakVal = i, cur
            else:
                cur = 1
                if i - peakIndex > peakVal - 1:
                    peakVal += 1
                    result += i - peakIndex
                else:
                    result += i - peakIndex - 1
            result += cur
        return result
