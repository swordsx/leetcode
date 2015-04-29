# import random, numpy
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        p0 = 0; p2 = len(A) - 1
        i = 0
        while i <= p2:
            if A[i] == 0:
                A[i], A[p0] = A[p0], A[i]
                p0 += 1
                i += 1
            elif A[i] == 2:
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1
            else:
                i += 1
                
# A = numpy.random.randint(0, 3, 15)
# print A
# Solution().sortColors(A)
# print A
