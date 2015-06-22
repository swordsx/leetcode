# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        head = TreeNode(preorder[0])
        self.index = 1
        mappreorder = {preorder[i] : i for i in range(len(preorder))}
        mapinorder = {inorder[i] : i for i in range(len(inorder))}
        
        def build(node):
            if self.index == len(preorder): return
            cur = preorder[self.index]
            if mapinorder[cur] < mapinorder[node.val]:
                node.left = TreeNode(cur)
                self.index += 1
                build(node.left)
                
            if self.index == len(preorder): return
            cur = preorder[self.index]
            shouldCreateRightChild = True
            for i in range(mapinorder[node.val] + 1, mapinorder[cur]):
                if mappreorder[inorder[i]] < self.index:
                    shouldCreateRightChild = False
                    break
            if shouldCreateRightChild:
                node.right = TreeNode(cur)
                self.index += 1
                build(node.right)
                
        build(head)
        return head
