class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        queue = collections.deque()
        result = []
        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            while queue and i - queue[0] >= k:
                queue.popleft()
            if i <= k - 2: continue
            curmax = nums[queue[0]]
            for j in range(1, len(queue)):
                curmax = max(curmax, nums[queue[1]])
            result.append(curmax)
        return result
