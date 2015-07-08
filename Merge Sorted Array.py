class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i = 0
        for j in range(n):
            while i < m + j and nums1[i] < nums2[j]:
                i += 1
            for k in range(m + j, i, -1):
                nums1[k] = nums1[k - 1]
            nums1[i] = nums2[j]
