from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        # Add all rotten oranges to the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        time = 0

        while q and fresh:
            for _ in range(len(q)):          # Process one level (one minute)
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2      # Mark as rotten
                        fresh -= 1
                        q.append((nr, nc))

            time += 1

        return time if fresh == 0 else -1
    