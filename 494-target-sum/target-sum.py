class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if abs(total)<abs(target) or (total+target)%2:
            return 0
        mod_target=(total+target)//2
        dp=[0]*(mod_target+1)
        dp[0]=1
        for num in nums:
            for s in range(mod_target,num-1,-1):
                dp[s]+=dp[s-num]
        return dp[mod_target]