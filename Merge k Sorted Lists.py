class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: heap.append(node)
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, node)
        return dummy.next
        
        
——————————————————
  
class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: heap.append((node.val, node))
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            node = heapq.heappop(heap)[1]
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val,node))
        return dummy.next  
