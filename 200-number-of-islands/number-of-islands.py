class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        output=0
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for _ in range(m)]
        directions=((0,1),(1,0),(-1,0),(0,-1))

        def dfs(i,j):
            visited[i][j]=1
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]=='1':
                    dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    output+=1
                    dfs(i,j)
        return output
                    

        