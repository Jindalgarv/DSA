class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * (i + 1) for i in range(n)]

        def solve(i, j):
            if i == 0 and j == 0:
                return triangle[0][0]

            if j < 0 or j > i:
                return float("inf")

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = triangle[i][j] + min(
                solve(i - 1, j),
                solve(i - 1, j - 1)
            )

            return dp[i][j]

        return min(solve(n - 1, j) for j in range(n))