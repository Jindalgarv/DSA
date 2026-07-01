class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        state=[0]*numCourses
        def dfs(node):
            if state[node]==1:
                return True
            if state[node]==2:
                return False
            state[node]=1
            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            state[node]=2
            return False
        for course in range(numCourses):
            if not state[course]:
                if dfs(course):
                    return False
        return True
        