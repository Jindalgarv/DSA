class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        def solve(i,target):
            if target==0:
                return 0
            if i==0:
                if target%coins[0]==0:
                    return target//coins[0]
                return float('inf')
            if dp[i][target]!=-1:
                return dp[i][target]
            
            notTaken=solve(i-1,target)
            taken=float('inf')
            if target>=coins[i]:
                taken=1+solve(i,target-coins[i])
            dp[i][target]= min(taken,notTaken)
            return dp[i][target]
        
        ans=solve(n-1,amount)
        return -1 if ans==float('inf') else ans

        