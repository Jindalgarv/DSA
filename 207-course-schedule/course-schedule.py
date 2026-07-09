class Solution:
    #basically have to check cycle only if it contains cycle then return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        visited=[0]*numCourses
        def dfs(node):
            if visited[node]==1:
                return True
            if visited[node]==2:
                return False
            visited[node]=1
            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            visited[node]=2
            
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True
            
                
