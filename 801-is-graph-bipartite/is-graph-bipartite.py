class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)

        def dfs(node):
            for adj in graph[node]:
                if color[adj]==-1:
                    color[adj]=1-color[node]
                    if not dfs(adj):
                        return False
                elif color[adj]==color[node]:
                    return False
            return True
    
        for i in range(len(graph)):
            if color[i]==-1:
                color[i]=0
                if not dfs(i):
                    return False
        return True

            