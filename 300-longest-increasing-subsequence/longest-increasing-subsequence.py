class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(n)]
        def solve(i,prev):
            if i==n:
                return 0
            if dp[i][prev+1]!=-1:
                return dp[i][prev+1]
            not_take=solve(i+1,prev)
            take=0
            if prev== -1 or nums[i]>nums[prev]:
                take=1+solve(i+1,i)
            dp[i][prev+1] = max(take,not_take)
            return dp[i][prev+1]
        return solve(0,-1)