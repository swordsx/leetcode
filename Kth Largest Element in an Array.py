import random
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        def partition(l, r):
            idx = random.randint(l, r)
            nums[idx], nums[r] = nums[r], nums[idx]
            i = l
            for j in range(l, r):
                if nums[j] > nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i + 1

        pos = 0; l = 0; r = len(nums) - 1
        while pos != k:
            if pos < k: l = pos
            else: r = pos - 1
            pos = partition(l, r)

        return nums[k - 1]
