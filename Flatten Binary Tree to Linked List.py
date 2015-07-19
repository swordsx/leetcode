# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root: return
        self.flatten(root.left)
        self.flatten(root.right)
        start, end = root.left, root.right
        if not start: return
        cur = start
        root.left = None
        while cur.right: cur = cur.right
        cur.right = end
        root.right = start
