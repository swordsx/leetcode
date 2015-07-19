# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head: return head
        fast = head
        length = 0
        while fast:
            length += 1
            fast = fast.next
        k %= length
        if k == 0: return head
        slow, fast = head, head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        ret = slow.next
        fast.next = head
        slow.next = None
        return ret
