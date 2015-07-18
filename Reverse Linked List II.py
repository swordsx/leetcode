# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if m == n: return head
        dummy = ListNode('#')
        dummy.next = head
        pre, cur, pos = dummy, head, 1
        while pos < m:
            pre, cur = pre.next, cur.next
            pos += 1
        tail = cur
        while pos <= n:
            post = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = post
            pos += 1
        tail.next = cur
        return dummy.next
