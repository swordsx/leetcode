class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        dp = {0:[[]]}
        for i in range(1, target + 1):
            combinations = []
            for candidate in candidates:
                if i - candidate in dp:
                    for combination in dp[i - candidate]:
                        combinations.append(combination + [candidate])
            dp[i] = combinations
        result = []
        for resultItem in dp[target]:
            resultItem.sort()
            if resultItem not in result:
                result.append(resultItem)
        return result
