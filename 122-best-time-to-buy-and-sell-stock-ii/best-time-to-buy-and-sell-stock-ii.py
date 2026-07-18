# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # for i in range(len(prices)-1):
        #     if prices[i]<prices[i+1]:
        #         profit+=prices[i+1]-prices[i]
        # return profit

#DP SOLUTION 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n=len(prices)
#         dp=[[-1]*2 for _ in range(n)]
#         profit=0
#         @cache
#         def solve(i,buy):
#             if i==n:
#                 return 0
#             if dp[i][buy]!=-1:
#                 return dp[i][buy]
#             if buy:
#                 profit=max(-prices[i]+solve(i+1,0),solve(i+1,1))
#             else:
#                 profit=max(prices[i]+solve(i+1,1),solve(i+1,0))
#             dp[i][buy]=profit
#             return dp[i][buy]
#         return solve(0,1)

#TABULATION CODE 

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n=len(prices)
#         dp=[[0]*2 for _ in range(n+1)]

#         for i in range(n-1,-1,-1):
#             dp[i][1]=max(-prices[i]+dp[i+1][0],dp[i+1][1])
#             dp[i][0]=max(prices[i]+dp[i+1][1],dp[i+1][0])
#         return dp[0][1]
                
#SPACE OPTIMISED TABULATION
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ahead = [0, 0]  # Represents dp[i+1]

        for i in range(len(prices) - 1, -1, -1):
            curr = [0, 0]

            curr[1] = max(
                -prices[i] + ahead[0],
                ahead[1]
            )

            curr[0] = max(
                prices[i] + ahead[1],
                ahead[0]
            )

            ahead = curr

        return ahead[1]
                

