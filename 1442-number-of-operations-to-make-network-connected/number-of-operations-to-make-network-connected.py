class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        visited=[0]*n
        graph=[[] for _ in range(n)]
        for i,j in connections:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i):
            visited[i]=1
            for nei in graph[i]:
                if not visited[nei]:
                    dfs(nei)
        ans=0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                ans+=1
        return ans-1
        