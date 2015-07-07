# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedArrayToBST(self, num):
        if not num:
            return None
        mid = len(num) / 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid + 1:])
        return root
    
    def sortedListToBST(self, head):
        num = []
        cur = head
        while cur:
            num.append(cur.val)
            cur = cur.next
        return self.sortedArrayToBST(num)
