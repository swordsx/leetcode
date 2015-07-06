# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        stack = [(root, 0)]
        result = []
        while stack:
            cur, depth = stack.pop(0)
            if cur:
                if len(result) == depth: result.append([])
                result[depth].append(cur.val)
                stack.append((cur.left, depth + 1))
                stack.append((cur.right, depth + 1))
        return result[::-1]
