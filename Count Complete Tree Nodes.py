# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root: return 0
        nodeL, nodeR = root.left, root.right
        heightL, heightR = 1, 1
        while nodeL: heightL, nodeL = heightL + 1, nodeL.left
        while nodeR: heightR, nodeR = heightR + 1, nodeR.right
        return (1 << heightL) - 1 if heightL == heightR else 1 + self.countNodes(root.left) + self.countNodes(root.right)
