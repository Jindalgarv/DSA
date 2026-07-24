class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.append(n),cuts.append(0)
        cuts.sort()
        dp=[[-1]*(c+1) for _ in range(c+1)]

        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+ solve(i,ind-1)+solve(ind+1,j)
                mini=min(mini,cost)
            dp[i][j]=mini
            return mini
        return solve(1,c)