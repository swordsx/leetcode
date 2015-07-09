class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combination(self, target, i, result):
        if i == len(self.candidates) or target < self.candidates[i]:
            return
        if self.candidates[i] == target and result + [self.candidates[i]] not in self.results:
            self.results.append(result + [self.candidates[i]])
            return

        self.combination(target, i + 1, result)
        self.combination(target - self.candidates[i], i + 1, result + [self.candidates[i]])
        
    def combinationSum2(self, candidates, target):
        self.results = []
        self.candidates = sorted(candidates)
        self.combination(target, 0, [])
        return self.results
