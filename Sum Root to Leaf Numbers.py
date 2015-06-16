# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    result = 0
    def sumNumbers(self, root):
        def sumNum(root, val):
            if not root: return
            val = val * 10 + root.val
            sumNum(root.left, val)
            sumNum(root.right, val)
            if (not root.left) and (not root.right):
                self.result += val
        sumNum(root, 0)
        return self.result
