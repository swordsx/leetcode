class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums: return False
        counter = collections.defaultdict(int)
        for num in nums:
            if counter[num] == 1:
                return True
            counter[num] += 1
        return False
