class Solution:
    #basically have to check cycle only if it contains cycle then return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for course,prereq in prerequisites:
            graph[prereq].append(course)
        visited=[0]*numCourses
        def dfs(i):
            if visited[i]==1:
                return True
            elif visited[i]==2:
                return False
            visited[i]=1
            for neighbour in graph[i]:
                if dfs(neighbour):
                    return True
            visited[i]=2
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True
        