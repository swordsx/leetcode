# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = ListNode("start")
        cur = head
        while l1 or l2:
            if l1 and l2 and l1.val < l2.val or not l2:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return head.next
    
    def sortList(self, head):
        if not head or not head.next: return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1, l2 = head, slow.next
        slow.next = None
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.mergeTwoLists(l1, l2)
