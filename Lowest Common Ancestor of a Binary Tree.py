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
    def postOrder(self, root, p, q):
        findP, findQ = False, False
        if not root: return root, findP, findQ
        node, findPL, findQL = self.postOrder(root.left, p, q)
        if findPL and findQL: return node, findPL, findQL
        node, findPR, findQR = self.postOrder(root.right, p, q)
        if findPR and findQR: return node, findPR, findQR
        findP = findPL or findPR
        findQ = findQL or findQR
        if root == p: findP = True
        if root == q: findQ = True
        return root, findP, findQ
       
    def lowestCommonAncestor(self, root, p, q):
        return self.postOrder(root, p, q)[0]
