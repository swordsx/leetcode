# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack = []; list = []
        cur = root
        while stack or cur:
            if not cur:
                (cur, visited) = stack.pop()
                    
                while visited == 'right':
                    list.append(cur.val)
                    if not stack:
                        return list
                    (cur, visited) = stack.pop()
                if visited == 'left':
                    stack.append((cur, 'right'))
                    cur = cur.right
            else:
                stack.append((cur, 'left'))
                cur = cur.left
        return list
