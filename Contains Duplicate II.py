class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dict = collections.defaultdict(list)
        for i in range(len(nums)):
            for index in dict[nums[i]]:
                if abs(index - i) <= k:
                    return True
            dict[nums[i]].append(i)
        return False
