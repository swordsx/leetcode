class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        primes = set(range(2, n))
        i = 2
        while i * i < n:
            if i in primes:
                j = (n - 1) / i
                while j >= i:
                    if j in primes:
                        primes.remove(i * j)
                    j -= 1
            i += 1
        return len(primes)
