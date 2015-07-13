class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        n1 = n2 = c1 = c2 = 0
        for num in nums:
            if num == n1: c1 += 1
            elif num == n2: c2 += 1
            elif c1 == 0: c1, n1 = 1, num
            elif c2 == 0: c2, n2 = 1, num
            else: c1, c2 = c1 - 1, c2 - 1
        result = []
        if nums.count(n1) > len(nums) / 3:
            result.append(n1)
        if nums.count(n2) > len(nums) / 3 and n1 != n2:
            result.append(n2)
        return result
