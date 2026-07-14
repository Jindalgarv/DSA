class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #RECURSIVE SOLUTION with MEMOIZATION
        # m,n=len(grid),len(grid[0])
        # dp=[[-1]*n for _ in range(m)]
        # def solve(i,j):
        #     if i==0 and j==0:
        #         return grid[0][0]
        #     elif i<0 or j<0:
        #         return float('inf')
        #     elif dp[i][j]!=-1:
        #         return dp[i][j]
        #     else:
        #         dp[i][j]=min(solve(i-1,j),solve(i,j-1))+grid[i][j]
        #         return dp[i][j]
        # return solve(m-1,n-1)
        
#TABULATION SOLUTION
#         m,n=len(grid),len(grid[0])
#         dp=[[0]*n for _ in range(m)]
#         dp[0][0]=grid[0][0]

#         for i in range(1,m):
#             dp[i][0]=dp[i-1][0]+grid[i][0]
#         for j in range(1,n):
#             dp[0][j]=dp[0][j-1]+grid[0][j]

#         for i in range(1,m):
#             for j in range(1,n):
#                 dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

#         return dp[m-1][n-1]


#TABULATION WITH SPACE OPTIMIZATION

        m, n = len(grid), len(grid[0])
        prev = [0] * n

        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[0][0]
                elif i == 0:
                    curr[j] = curr[j - 1] + grid[i][j]
                elif j == 0:
                    curr[j] = prev[j] + grid[i][j]
                else:
                    curr[j] = min(prev[j], curr[j - 1]) + grid[i][j]
            prev = curr

        return prev[-1]