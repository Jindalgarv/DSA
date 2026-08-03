from math import comb

class Solution:

    # =====================================================
    # 1. RECURSION
    # Time  : O(2^(m+n))
    # Space : O(m+n)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            elif i>m-1 or j>n-1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]= dfs(i+1,j)+dfs(i,j+1)
            return dp[i][j]
        return dfs(0,0)