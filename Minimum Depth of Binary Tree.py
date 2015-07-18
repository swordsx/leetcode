# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if not node: continue
            if not node.left and not node.right: return depth
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
        return 0
