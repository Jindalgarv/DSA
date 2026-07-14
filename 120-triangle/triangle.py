class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#RESCURSIVE WITH MEMOIZATION
        # n = len(triangle)
        # dp = [[-1] * (i + 1) for i in range(n)]

        # def solve(i, j):
        #     if i == 0 and j == 0:
        #         return triangle[0][0]

        #     if j < 0 or j > i:
        #         return float("inf")

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     dp[i][j] = triangle[i][j] + min(
        #         solve(i - 1, j),
        #         solve(i - 1, j - 1)
        #     )

        #     return dp[i][j]

        # return min(solve(n - 1, j) for j in range(n))

#TABULATION METHOD
        n = len(triangle)
        dp = [[0]*(i+1) for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if i==0 and j==0:
                    dp[i][j]=triangle[0][0]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==i:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[n-1])