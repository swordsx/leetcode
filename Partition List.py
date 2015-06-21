# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        newHead1 = ListNode('new1')
        newHead2 = ListNode('new2')
        cur1 = newHead1
        cur2 = newHead2
        cur = head
        while cur:
            if cur.val >= x:
                cur2.next = ListNode(cur.val)
                cur2 = cur2.next
            else:
                cur1.next = ListNode(cur.val)
                cur1 = cur1.next
            cur = cur.next
        cur1.next = newHead2.next        
        return newHead1.next
