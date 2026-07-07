class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n=len(grid)
        directions=((1,1),(1,0),(0,1),(1,-1),(-1,1),(-1,-1),(0,-1),(-1,0))
        distance=[[float('inf')]*n for _ in range(n)]
        distance[0][0]=0
        q=deque()
        q.append((0,0,0))
        while q:
            dis,r,c=q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and not grid[nr][nc] and distance[nr][nc]>1+dis:
                    distance[nr][nc]=1+dis
                    q.append((dis+1,nr,nc))
        if distance[n-1][n-1]<float('inf'):
            return distance[n-1][n-1]+1
        return -1

