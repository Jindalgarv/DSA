class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        buy=0
        while(buy<n):
            days=1
            while(buy+1<n and prices[buy]>=prices[buy+1]):
                buy+=1
            if(buy==n-1):
                break
            sell=buy+1
            while(sell+1<n and prices[sell]<=prices[sell+1]):
                sell+=1
            profit+=prices[sell]-prices[buy]
            buy=sell+1
        return profit
        
            
        