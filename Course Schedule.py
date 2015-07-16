class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        def dfs(vertex):
            visited[vertex] = 1
            for endVertex in edges[vertex]:
                if visited[endVertex] == 1: return False
                elif visited[endVertex] == 0 and dfs(endVertex) == False:
                    return False
            visited[vertex] = 2
            return True
            
        edges = [[] for i in range(numCourses)]
        for edge in prerequisites:
            edges[edge[0]].append(edge[1])
        visited = [0] * numCourses
        for vertex in range(numCourses):
            if visited[vertex] == 0 and dfs(vertex) == False:
                return False
        return True
