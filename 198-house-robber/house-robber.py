class Solution:
    def rob(self, nums: List[int]) -> int:
        # def solve(i):
        #     if i <0:
        #         return 0
        #     elif i==0:
        #         return nums[0]
        #     if dp[i]!=-1:
        #         return dp[i]
        #     pick= nums[i]+ solve(i-2)
        #     notPick=solve(i-1)
        #     dp[i]=max(pick,notPick)
        #     return dp[i]

        # n=len(nums)
        # dp=[-1]*n
        # return solve(n-1)
        if len(nums)==1:
            return nums[0]
        prev2,prev1=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            curr=max(nums[i]+prev2,prev1)
            prev2,prev1=prev1,curr
        return prev1
        