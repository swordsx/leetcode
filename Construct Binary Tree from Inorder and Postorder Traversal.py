# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def build(self, iBegin, iEnd, pBegin, pEnd):
        #print iBegin, iEnd, pBegin, pEnd
        if pBegin > pEnd: return None
        root = TreeNode(self.postorder[pEnd])
        index = self.mapinorder[root.val]
        leftLen = index - 1 - iBegin
        rightLen = iEnd - index - 1
        root.left = self.build(iBegin, index - 1, pBegin, pBegin + leftLen)
        root.right = self.build(index + 1, iEnd, pEnd - 1 - rightLen, pEnd - 1)
        return root
        
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        self.mapinorder = {inorder[i] : i for i in range(len(inorder))}
        return self.build(0, len(inorder) - 1, 0, len(postorder) - 1)
