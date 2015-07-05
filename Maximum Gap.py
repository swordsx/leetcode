class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        if len(nums) < 2: return 0
        B, A, N = max(nums), min(nums), len(nums)
        bucketLen = (B - A + N - 2) / (N - 1)   #ceil(x/y) = (x+y-1)/y
        bucket = {}
        for num in nums:
            loc = (num - A) / bucketLen
            if loc not in bucket:
                bucket[loc] = (num, num)
            else:
                bucket[loc] = (min(num, bucket[loc][0]), max(num, bucket[loc][1]))
        curMin, curMax = bucket[0]
        result = curMax - curMin
        for loc in range(N):
            if loc in bucket:
                result = max(bucket[loc][0] - curMax, result)
                curMin, curMax = bucket[loc]
        return result
