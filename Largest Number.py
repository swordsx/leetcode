class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(str1, str2):
            if len(str1) > len(str2):
                return 0 - compare(str2, str1)
            i, j = 0, 0
            while j < len(str2) and str1[i] == str2[j]:
                i, j = (i + 1) % len(str1), j + 1
            j %= len(str2)
            cha, chb = str1[i], str2[j]
            if cha == chb: return 0
            elif cha < chb: return -1
            else: return 1
        if sum(nums) == 0: return '0'
        strnums = [str(num) for num in nums]
        strnums.sort(cmp = compare, reverse = True)
        result = ''.join(strnums)
        return result
