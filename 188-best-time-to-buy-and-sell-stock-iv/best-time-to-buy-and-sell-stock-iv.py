class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        cap = k

        dp = [[[0] * (cap + 1) for _ in range(2)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for can_buy in range(2):
                for c in range(1, cap + 1):
                    if can_buy:
                        buy = -prices[i] + dp[i + 1][0][c]
                        skip = dp[i + 1][1][c]
                        dp[i][1][c] = max(buy, skip)
                    else:
                        sell = prices[i] + dp[i + 1][1][c - 1]
                        hold = dp[i + 1][0][c]
                        dp[i][0][c] = max(sell, hold)

        return dp[0][1][cap]

        