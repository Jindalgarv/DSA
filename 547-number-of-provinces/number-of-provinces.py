class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited[i]=1
            for x in adjLs[i]:
                if not visited[x]:
                    dfs(x)
        count=0
        n=len(isConnected)
        adjLs=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i!=j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        visited=[0]*n
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
        return count


        