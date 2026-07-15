class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if sum(nums)%2:
            return False
        target=sum(nums)//2

        prev=[False]*(target+1)
        prev[0]=True

        if nums[0]<=target:
            prev[nums[0]]=True

        for i in range(1,n):
            curr=[False]*(target+1)
            curr[0]=True

            for t in range(1,target+1):
                notTaken=prev[t]
                taken=False

                if nums[i]<=t:
                    taken=prev[t-nums[i]]
                curr[t]=taken or notTaken
            prev=curr
        return prev[target]
