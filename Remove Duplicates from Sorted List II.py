# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy = ListNode('#')
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            post = cur.next
            if post and cur.val == post.val:
                val = cur.val
                while post and post.val == val:
                    post = post.next
                pre.next = post
                cur = post
            else:
                pre = cur
                cur = post
        return dummy.next
