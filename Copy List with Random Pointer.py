# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def dfs(self, inputNode, map):
        if not inputNode: return inputNode
        if inputNode in map:
            return map[inputNode]
        outputNode = RandomListNode(inputNode.label)
        map[inputNode] = outputNode
        outputNode.next = self.dfs(inputNode.next, map)
        outputNode.random = self.dfs(inputNode.random, map)
        return outputNode
        
    def copyRandomList(self, head):
        if not head: return None
        return self.dfs(head, {})
