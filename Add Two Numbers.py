# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        carry = 0; val1 = 0; val2 = 0
        head = ListNode(-1)
        cur = head
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else: val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else: val2 = 0
            cur.next = ListNode((val1 + val2 + carry) % 10)
            carry = (val1 + val2 + carry) / 10
            cur = cur.next
        if carry:
            cur.next = ListNode(1)
        return head.next
