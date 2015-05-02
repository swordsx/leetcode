# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        def BFSLeft(root):
            list = []
            queue = [root]
            while queue:
                cur = queue.pop(0)
                if cur:
                    list.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    list.append(None)
            return list
        def BFSRight(root):
            list = []
            queue = [root]
            while queue:
                cur = queue.pop(0)
                if cur:
                    list.append(cur.val)
                    queue.append(cur.right)
                    queue.append(cur.left)
                else:
                    list.append(None)
            return list
        return BFSLeft(root) == BFSRight(root)
