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
        if root is None:
            return
        queue = [root]
        i = 0
        while i < len(queue):
            if queue[i].left is not None:
                queue.append(queue[i].left)
            if queue[i].right is not None:
                queue.append(queue[i].right)
            if i < len(queue) - 1:
                queue[i].next = queue[i + 1]
            i += 1
        cur = root
        while cur is not None:
            cur.next = None
            cur = cur.right
