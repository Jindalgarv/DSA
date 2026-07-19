class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #DP SOLUTION 
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        profit=0
        def solve(i,buy):
            if i==n or i==n+1:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                profit=max(-prices[i]+solve(i+1,0),solve(i+1,1))
            else:
                profit=max(prices[i]+solve(i+2,1),solve(i+1,0))
            dp[i][buy]=profit
            return dp[i][buy]
        return solve(0,1)
        