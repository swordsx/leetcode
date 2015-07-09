class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findKth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        
        index1 = min(k / 2, m)
        index2 = k - index1
        if nums1[index1 - 1] == nums2[index2 - 1]:
            return nums1[index1 - 1]
        elif nums1[index1 - 1] < nums2[index2 - 1]:
            return self.findKth(nums1[index1:], nums2, k - index1)
        else:
            return self.findKth(nums1, nums2[index2:], k - index2)
        
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.findKth(nums1, nums2, (m + n + 1) / 2)
        else:
            return (self.findKth(nums1, nums2, (m + n) / 2) +
                    self.findKth(nums1, nums2, (m + n) / 2 + 1)) / 2.0
