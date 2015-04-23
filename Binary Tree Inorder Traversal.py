# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        list = []
        cur = root
        while len(stack) is not 0 or cur is not None:
            while cur.left is not None:
                stack.append(cur)
                cur = cur.left
            list.append(cur.val)
            while cur.right is None:
                if len(stack) is not 0:
                    cur = stack.pop()
                    list.append(cur.val)
                else:
                    break;
            if cur is not None:
                cur = cur.right
                    
        return list
