class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        visited = {num : False for num in nums}
        result = 0
        for num in visited:
            if visited[num]: continue
            curlen = 1
            up, down = num + 1, num - 1
            while up in visited:
                visited[up] = True
                up += 1
                curlen += 1
            while down in visited:
                visited[down] = True
                down -= 1
                curlen += 1
            visited[num] = True
            result = max(result, curlen)
        return result
