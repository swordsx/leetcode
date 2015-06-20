class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        def combinSum(k, n, candidates, startWith):
            #print k, n, candidates
            if k < 0 or n < 0: return
            if k == 0 and n == 0:
                result = []
                for i in range(1, 10):
                    if candidates[i] == False:
                        result.append(i)
                if result not in self.results:
                    self.results.append(result)
            for i in range(startWith, 10):
                if candidates[i] == True:
                    candidates[i] = False
                    combinSum(k - 1, n - i, candidates, startWith + 1)
                    candidates[i] = True
            return
        candidates = [True] * 10
        self.results = []
        combinSum(k, n, candidates, 1)
        return self.results
