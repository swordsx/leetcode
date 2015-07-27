class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        def parse(input):
            num = 0
            nums, ops = [], []
            for ch in input:
                if ch in '+-*':
                    nums.append(num)
                    ops.append(ch)
                    num = 0
                else:
                    num = num * 10 + int(ch)
            nums.append(num)
            return nums, ops
        nums, ops = parse(input)

        n = len(nums)
        dp = [[[] for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[0][i].append(nums[i])
        for i in range(1, n):
            for j in range(0, n - i):
                for k in range(i):
                    for num1 in dp[k][j]:
                        for num2 in dp[i - k - 1][k + j + 1]:
                            if ops[k+j] == '+': dp[i][j].append(num1 + num2)
                            elif ops[k+j] == '-': dp[i][j].append(num1 - num2)
                            else: dp[i][j].append(num1 * num2)
        return sorted(dp[n - 1][0])
