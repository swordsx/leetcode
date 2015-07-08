# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        dummy = ListNode('#')
        cur = head
        last = cur
        while cur:
            post = cur.next
            pre = dummy
            if cur.val > last.val:  #to pass the [0...4999] case
                pre = last
            else:
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
            cur.next = pre.next
            pre.next = cur
            if not cur.next:
                last = cur
            cur = post
        return dummy.next
