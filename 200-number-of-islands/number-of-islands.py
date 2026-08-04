class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #IF WANT TO OPTIMIZE THE SPACE WE CAN JUST MODIFY THE GRID
        # m,n=len(grid),len(grid[0])
        # directions=[(-1,0),(0,1),(1,0),(0,-1)]
        # def dfs(i,j):
        #     grid[i][j]='0'
        #     for dr,dc in directions:
        #         nr=i+dr
        #         nc=j+dc
        #         if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='0':
        #             dfs(nr,nc)

        # count=0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]=='1':
        #             dfs(i,j)
        #             count+=1
        # return count
        m,n=len(grid),len(grid[0])
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        q=deque()
        count=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    grid[i][j]='0'
                    q.append((i,j))
                    count+=1
                    while q:
                        r,c=q.popleft()
                        for dr,dc in directions:
                            nr,nc=r+dr,c+dc
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                                grid[nr][nc]='0'
                                q.append((nr,nc))
        return count



        

