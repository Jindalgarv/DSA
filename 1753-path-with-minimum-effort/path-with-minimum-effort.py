class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq=[(0,0,0)]
        m,n=len(heights),len(heights[0])
        min_effort=[[float('inf')]*n for _ in range(m)]
        min_effort[0][0]=0

        directions=((0,1),(1,0),(-1,0),(0,-1))
        
        while pq:
            effort,row,col=heappop(pq)
            if row==m-1 and col==n-1:
                return effort
            if effort>min_effort[row][col]:
                continue
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n:
                    edge_effort = abs(heights[row][col] - heights[nr][nc])
                    new_effort = max(effort, edge_effort)

                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_effort
                        heappush(pq, (new_effort, nr, nc))


