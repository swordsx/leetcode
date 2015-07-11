# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def helper(self, root, sum, result):
        if not root: return
        if not root.left and not root.right and sum == root.val:
            self.results.append(result + [root.val])
            return 
        self.helper(root.left, sum - root.val, result + [root.val])
        self.helper(root.right, sum - root.val, result + [root.val])
    def pathSum(self, root, sum):
        self.results = []
        self.helper(root, sum, [])
        return self.results
