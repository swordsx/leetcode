class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        lenNums = len(nums)
        for i in range(1 << lenNums):
            item = []
            for bit in range(lenNums):
                if i & (1 << bit):
                    item.append(nums[bit])
            if item not in result:
                result.append(item)
        return result
