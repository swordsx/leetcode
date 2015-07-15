# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def postOrder(self, root):
        if not root: return 0
        leftMax = self.postOrder(root.left)
        rightMax = self.postOrder(root.right)
        self.result = max(self.result, leftMax + rightMax + root.val)
        return max(0, leftMax + root.val, rightMax + root.val)
    def maxPathSum(self, root):
        self.result = -0x80000000
        self.postOrder(root)
        return self.result
