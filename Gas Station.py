class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        result, rest = 0, 0
        for i in range(len(gas)):
            rest += gas[i] - cost[i]
            if rest < 0:
                result = i + 1
                rest = 0
        return result
