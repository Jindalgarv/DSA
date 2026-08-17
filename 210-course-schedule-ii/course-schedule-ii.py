    #just check topological sort and return it 
    #use kahn's algorithm
class Solution:
    def findOrder(
        self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        order = []
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        for node,deg in enumerate(indegree):
            if deg==0:
                q.append(node)

        while q:
            node =q.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(order)==numCourses:
            return order
        return []
                
