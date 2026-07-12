class Solution:

    # =====================================================
    # SPACE OPTIMIZED DP
    # Time  : O(m*n)
    # Space : O(n)
    # =====================================================
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        prev = [0] * n

        for i in range(m):

            curr = [0] * n

            for j in range(n):

                # Current cell is blocked
                if obstacleGrid[i][j]:
                    curr[j] = 0

                # Starting cell
                elif i == 0 and j == 0:
                    curr[j] = 1

                else:
                    up = prev[j]
                    left = curr[j - 1] if j > 0 else 0
                    curr[j] = up + left

            prev = curr

        return prev[-1]