class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i = 0
        for num in A:
            if num != elem:
                A[i] = num
                i += 1
        return i
