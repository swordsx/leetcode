# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        pA, pB = headA, headB
        IFPA, IFPB = True, True     #isFirstPassA, isFirstPassB
        while True:
            if pA == pB and not IFPA: return pA
            if pA: pA = pA.next
            else: pA, IFPA = headB, False
            if pB: pB = pB.next
            else: pB, IFPB = headA, False
