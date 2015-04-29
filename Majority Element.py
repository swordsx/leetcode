class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        dict = collections.defaultdict(int)
        for num in nums:
            dict[num] += 1
        for num in dict:
            if dict[num] > len(nums) / 2:
                return num
