class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSumClosest(self, nums, target):
        result = sum(nums[:3])

        nums.sort()
        lenNums = len(nums)
        for i in range(lenNums - 2):
            j, k = i + 1, lenNums - 1
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]
                if Sum == target:
                    return target
                elif Sum < target:
                    j += 1
                else:
                    k -= 1
                if abs(Sum - target) < abs(result - target):
                    result = Sum
        return result
