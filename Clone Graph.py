# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def dfs(self, inputNode, map):
        if inputNode in map:
            return map[inputNode]
        outputNode = UndirectedGraphNode(inputNode.label)
        map[inputNode] = outputNode
        for node in inputNode.neighbors:
            outputNode.neighbors.append(self.dfs(node, map))
        return outputNode
    
    def cloneGraph(self, node):
        if not node: return None
        return self.dfs(node, {})
