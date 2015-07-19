class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        def dfs(vertex):
            visited[vertex] = 1
            for endVertex in edges[vertex]:
                if visited[endVertex] == 1: return False
                elif visited[endVertex] == 0 and dfs(endVertex) == False:
                    return False
            visited[vertex] = 2
            order[self.timestamp] = vertex
            self.timestamp -= 1
            return True
            
        edges = [[] for i in range(numCourses)]
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
        visited = [0] * numCourses
        self.timestamp = numCourses - 1
        order = [-1] * numCourses
        for vertex in range(numCourses):
            if visited[vertex] == 0 and dfs(vertex) == False:
                return []
        return order
