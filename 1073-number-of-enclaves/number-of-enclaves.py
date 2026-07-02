class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        count=0
        directions=((0,1),(1,0),(-1,0),(0,-1))

        def dfs(i,j):
            grid[i][j]=2
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                if 0<nr<m-1 and 0<nc<n-1 and grid[nr][nc]==1 :
                    dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and grid[i][j]==1:
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
        return count
                    


        