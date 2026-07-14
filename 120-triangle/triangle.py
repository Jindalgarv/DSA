class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[float('inf')]*n for _ in range(n)]
        
        def solve(i,j):
            if i==0:
                return triangle[0][0]
            if i<0 or j<0 or j>i:
                return float('inf')
            if dp[i][j]!=float('inf'):
                return dp[i][j]
            else:
                dp[i][j]=min(solve(i-1,j),solve(i-1,j-1))+triangle[i][j]
                return dp[i][j]
        
        output=float('inf')
        for j in range(n):
            output=min(output,solve(n-1,j))
        return output

        