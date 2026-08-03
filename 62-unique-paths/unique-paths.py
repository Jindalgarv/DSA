from math import comb

class Solution:

    # =====================================================
    # 1. RECURSION
    # Time  : O(2^(m+n))
    # Space : O(m+n)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:
        # dp=[[0]*n for _ in range(m)]
        # for i in range(m):
        #     dp[i][0]=1
        # for j in range(n):
        #     dp[0][j]=1
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # return dp[m-1][n-1]
        prev=[1]*n
        for i in range(1,m):
            curr=[1]*n
            for j in range(1,n):
                curr[j]=prev[j]+curr[j-1]
            prev=curr
        return prev[-1]