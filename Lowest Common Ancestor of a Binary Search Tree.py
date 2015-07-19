# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def binarySearch(self, root, node):
        if not root: return
        if root.val == node.val: return [root]
        elif root.val > node.val: return [root] + self.binarySearch(root.left, node)
        else: return [root] + self.binarySearch(root.right, node)
        
    def lowestCommonAncestor(self, root, p, q):
        pathP = self.binarySearch(root, p)
        pathQ = self.binarySearch(root, q)
        result = None
        if not pathP or not pathQ: return None
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] == pathQ[i]:
                result = pathP[i]
        return result
