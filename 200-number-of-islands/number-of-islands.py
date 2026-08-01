class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #IF WANT TO OPTIMIZE THE SPACE WE CAN JUST MODIFY THE GRID
        m,n=len(grid),len(grid[0])
        visited=[[0]*n for _ in range(m)]
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(i,j):
            visited[i][j]=1
            for dr,dc in directions:
                nr=i+dr
                nc=j+dc
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]=='1':
                    dfs(nr,nc)

        count=0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count
        

