class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
        def solve(i,canbuy,cap):
            if i==n or cap==0:
                return 0
            if dp[i][canbuy][cap]!=-1:
                return dp[i][canbuy][cap]
            if canbuy:
                dp[i][canbuy][cap]=max(-prices[i]+solve(i+1,0,cap),solve(i+1,1,cap))
            else:
                dp[i][canbuy][cap]=max(prices[i]+solve(i+1,1,cap-1),solve(i+1,0,cap))
            return dp[i][canbuy][cap]
        return solve(0,1,2)