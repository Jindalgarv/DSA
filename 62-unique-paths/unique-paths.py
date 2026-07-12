# from math import factorial
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))

from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        dp[0][0]=1
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=solve(i-1,j)
            left=solve(i,j-1)
            dp[i][j]=solve(i-1,j)+ solve(i,j-1)
            return dp[i][j]
        return solve(m-1,n-1)