class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        def swap(k, pos):
            #print k, pos, nums
            if k == 0: return
            if pos >= 2 * k:
                for i in range(k):
                    nums[pos-i], nums[pos-i-k] = nums[pos-i-k], nums[pos-i]
                swap(k, pos - k)
            else:
                for i in range(pos - k + 1):
                    nums[i], nums[i+k] = nums[i+k], nums[i]
                swap(2 * k - pos - 1, k - 1)
        k %= len(nums)
        swap(k, len(nums) - 1)        
