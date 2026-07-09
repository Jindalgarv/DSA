from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        directions=((0,1),(0,-1),(1,0),(-1,0))
        q=deque()
        m,n= len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,time))
        while q:
            row,col,t=q.popleft()
            time=t
            for dr,dc in directions:
                nr,nc=row+dr,col+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    q.append((nr,nc,t+1))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return time



