class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #DP SOLUTION 
        # n=len(prices)
        # dp=[[-1]*2 for _ in range(n)]
        # def solve(i,buy):
        #     if i==n or i==n+1:
        #         return 0
        #     if dp[i][buy]!=-1:
        #         return dp[i][buy]
        #     if buy:
        #         dp[i][buy]=max(-prices[i]+solve(i+1,0),solve(i+1,1))
        #     else:
        #         dp[i][buy]=max(prices[i]+solve(i+2,1),solve(i+1,0))
        #     return dp[i][buy]
        # return solve(0,1)

#MEMOIZATION 
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            dp[i][1]=max(-prices[i]+dp[i+1][0],dp[i+1][1])
            dp[i][0]=max(prices[i]+dp[i+2][1],dp[i+1][0])
        return dp[0][1]



