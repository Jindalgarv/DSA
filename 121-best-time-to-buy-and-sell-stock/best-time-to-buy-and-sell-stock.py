class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest=float('inf')
        for x in prices:
            lowest=min(x,lowest)
            max_profit=max(max_profit,x-lowest)
        return max_profit

            
        
        