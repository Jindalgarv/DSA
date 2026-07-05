class Solution:
    #just check topological sort and return it 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q=deque()
        indegree=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        output=[]

        for u,v in prerequisites:
            graph[v].append(u)

        for u,v in prerequisites:
            indegree[u]+=1
        for i,x in enumerate(indegree):
            if not x:
                q.append(i)
        while q:
            node=q[0]
            output.append(q.popleft())
            for x in graph[node]:
                indegree[x]-=1
                if indegree[x]==0:
                    q.append(x)
        if len(output)==numCourses:
            return output
        return []
                