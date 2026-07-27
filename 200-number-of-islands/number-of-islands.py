class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j):
            visited[i][j] = True

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (0 <= nr < m and
                    0 <= nc < n and
                    not visited[nr][nc] and
                    grid[nr][nc] == "1"):
                    dfs(nr, nc)

        islands = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands