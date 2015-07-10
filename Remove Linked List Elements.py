# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode('#')
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            post = cur.next
            if cur.val == val:
                pre.next = cur.next
                cur = post
            else:
                pre = cur
                cur = post
        return dummy.next
