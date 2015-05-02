# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = [(root, 1)]
        i = 0
        while i < len(queue):
            curNode, curDepth = queue[i]
            if curNode.left:
                queue.append((curNode.left, curDepth + 1))
            if curNode.right:
                queue.append((curNode.right, curDepth + 1))
            i += 1
        for i in range(len(queue) - 1):
            if queue[i][1] == queue[i + 1][1]:
                queue[i][0].next = queue[i + 1][0]
