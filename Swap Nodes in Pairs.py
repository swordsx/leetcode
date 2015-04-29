# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        start = ListNode('Hello World')
        start.next = head
        pre = start
        cur = head
        while cur:
            post = cur.next
            if post:
                pre.next = post
                cur.next = post.next
                post.next = cur
            pre = cur
            cur = cur.next
        return start.next
