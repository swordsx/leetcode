# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBSTwithMINandMAX(self, root):
        if not root: return (True, None, None)
        (flagL, minL, maxL) = self.isValidBSTwithMINandMAX(root.left)
        (flagR, minR, maxR) = self.isValidBSTwithMINandMAX(root.right)
        flagRET, minRET, maxRET = flagL and flagR, root.val, root.val
        if flagRET == False: return (False, None, None)
        if maxL is not None:
            if maxL >= root.val: return (False, None, None)
        if minR is not None:
            if minR <= root.val: return (False, None, None)
        if minL is not None:
            minRET = min(minL, minRET)
        if maxR is not None:
            maxRET = max(maxR, maxRET)
        print root.val, minRET, maxRET
        return True, minRET, maxRET
        
    def isValidBST(self, root):
        return self.isValidBSTwithMINandMAX(root)[0]
