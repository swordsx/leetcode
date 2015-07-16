# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head: return True
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        post = slow.next
        slow.next = None
        pre, slow = slow, post
        while slow:
            post = slow.next
            slow.next = pre
            pre, slow = slow, post
        tail = pre
        while head and tail:
            if head.val == tail.val:
                head, tail = head.next, tail.next
            else: return False

        return True
