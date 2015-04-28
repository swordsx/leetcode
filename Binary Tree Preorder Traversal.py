# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack = [root]
        list = []
        while stack:
            cur = stack.pop()
            if cur:
                list.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return list
