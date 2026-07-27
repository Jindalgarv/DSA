class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        pacific=set()
        atlantic=set()

        def dfs(i,j,visited):
            visited.add((i,j))
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                if 0<=nr<m and 0<=nc<n and ((nr,nc) not in visited)and heights[nr][nc]>=heights[i][j]:
                    dfs(nr,nc,visited)

        for i in range(m):
            if (i,0) not in pacific:
                dfs(i,0,pacific)
            if (i,n-1) not in atlantic:
                dfs(i,n-1,atlantic)

        for j in range(n):
            if (0,j) not in pacific:
                dfs(0,j,pacific)
            if (m-1,j) not in atlantic:
                dfs(m-1,j,atlantic)

        return [list(cell) for cell in pacific & atlantic]
                    
