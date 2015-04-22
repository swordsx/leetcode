# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)
        return max(depthLeft, depthRight) + 1
