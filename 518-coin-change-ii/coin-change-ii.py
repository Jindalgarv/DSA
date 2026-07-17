class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def solve(i,target):
            if i==0:
                if not target%coins[i]:
                    return 1
                return 0
            if dp[i][target]!=-1:
                return dp[i][target]
            not_taken=solve(i-1,target)
            taken=0
            if coins[i]<=target:
                taken=solve(i,target-coins[i])
            dp[i][target]=taken+not_taken
            return dp[i][target]
        return solve(n-1,amount)