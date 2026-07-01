from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # -----------------------------
        # Step 1: Multi-source BFS
        # -----------------------------
        dist = [[-1] * n for _ in range(n)]
        queue = deque()

        # Add all thieves as starting points
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and dist[nr][nc] == -1
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # -----------------------------
        # Step 2: Dijkstra (Max Heap)
        # -----------------------------
        max_heap = [(-dist[0][0], 0, 0)]

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while max_heap:

            neg_safe, r, c = heapq.heappop(max_heap)

            current_safe = -neg_safe

            # Reached destination
            if r == n - 1 and c == n - 1:
                return current_safe

            for dr, dc in directions:

                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and not visited[nr][nc]
                ):

                    new_safe = min(current_safe, dist[nr][nc])

                    heapq.heappush(
                        max_heap,
                        (-new_safe, nr, nc)
                    )

                    visited[nr][nc] = True

        return 0