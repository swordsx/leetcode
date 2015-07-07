# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root: return []
        queue = [(root, 1)]
        result = []
        i = 0
        while i < len(queue):
            cur, depth = queue[i]
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))
            i += 1
        for i in range(len(queue)):
            if i == len(queue) - 1 or queue[i][1] == queue[i + 1][1] - 1:
                result.append(queue[i][0].val)
        return result
