# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        #if not head: return head
        list1, list2 = [], []
        slow, fast = head, head
        while fast and fast.next:
            list1.append(slow)
            slow = slow.next
            fast = fast.next.next
        while slow:
            list2.append(slow)
            slow = slow.next
        list2.reverse()

        i = 0
        while True:
            if i == len(list2): break
            if i == len(list1):
                list2[i].next = None
                break
            list1[i].next = list2[i]
            if i < len(list1) - 1: list2[i].next = list1[i + 1]
            elif i < len(list2) - 1: list2[i].next = list2[i + 1]
            else: list2[i].next = None
            i += 1
        cur = head
