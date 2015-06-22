# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        queue = [(root, 0)]
        result = []
        i = 0
        while i < len(queue):
            (node, depth) = queue[i]
            i += 1
            if not node: continue
            if depth >= len(result):
                result.append([])
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
            result[depth].append(node.val)

        for i in range(len(result)):
            if i % 2 == 1:
                result[i].reverse()
        return result
