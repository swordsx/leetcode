# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        exist = {}
        cur = head
        while cur is not None:
            if cur in exist:
                return True
            exist[cur] = True
            cur = cur.next
        return False

class Solution2:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 
