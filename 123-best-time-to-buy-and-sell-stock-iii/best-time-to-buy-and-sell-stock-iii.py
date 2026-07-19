class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cap = 2

        dp = [[[-1] * (cap + 1) for _ in range(2)] for _ in range(n)]

        def solve(i, can_buy, cap):
            if i == n or cap == 0:
                return 0

            if dp[i][can_buy][cap] != -1:
                return dp[i][can_buy][cap]

            if can_buy:
                buy = -prices[i] + solve(i + 1, 0, cap)
                skip = solve(i + 1, 1, cap)
                dp[i][can_buy][cap] = max(buy, skip)
            else:
                sell = prices[i] + solve(i + 1, 1, cap - 1)
                hold = solve(i + 1, 0, cap)
                dp[i][can_buy][cap] = max(sell, hold)

            return dp[i][can_buy][cap]

        return solve(0, 1, cap)