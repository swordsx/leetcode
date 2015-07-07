# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverse(self, head, tail):
        pre, cur = head, head.next
        while pre is not tail:
            post = cur.next
            cur.next = pre
            pre, cur = cur, post
        return tail, head
        
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        begin, cur = dummy, head
        n = 0
        while cur:
            n += 1
            if n % k == 0:
                end = cur.next
                newHead, newTail = self.reverse(begin.next, cur)
                begin.next.next = end
                begin.next, cur = cur, begin.next
                begin = cur
            cur = cur.next
        return dummy.next
