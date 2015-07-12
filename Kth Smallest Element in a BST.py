# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def inOrder(self, root, k):
        if not root: return
        left = self.inOrder(root.left, k)
        if left != None: return left
        self.count += 1
        if self.count == k: return root.val
        right = self.inOrder(root.right, k)
        if right != None: return right
        
    def kthSmallest(self, root, k):
        self.count = 0
        return self.inOrder(root, k)
