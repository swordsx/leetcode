# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def DFS(self, root):
        if not root: return
        self.DFS(root.left)
        if self.pre and root.val < self.pre.val:
            if not self.node1:
                self.node1, self.node2 = self.pre, root
            else:
                self.node2 = root
        self.pre = root
        self.DFS(root.right)
    def recoverTree(self, root):
        self.pre = None
        self.node1, self.node2 = None, None
        self.DFS(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
