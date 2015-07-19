# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def dfs(self, start, end):
        if start > end: return [None]
        result = []
        for i in range(start, end + 1):
            subLeft = self.dfs(start, i - 1)
            subRight = self.dfs(i + 1, end)
            for rootLeft in subLeft:
                for rootRight in subRight:
                    root = TreeNode(i)
                    root.left = rootLeft
                    root.right = rootRight
                    result.append(root)
        return result
    def generateTrees(self, n):
        return self.dfs(1, n)
