class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        results = []
        lenNums = len(nums)
        dict = collections.defaultdict(list)
        for i in range(lenNums):
            for j in range(i + 1, lenNums):
                dict[nums[i] + nums[j]].append(set([i, j]))
        for twoSum in dict:
            if target - twoSum in dict:
                for set1 in dict[twoSum]:
                    for set2 in dict[target - twoSum]:
                        setUnion = set1 | set2
                        if len(setUnion) == 4:
                            result = sorted([nums[i] for i in setUnion])
                            if result not in results:
                                results.append(result)
                        
        return results
