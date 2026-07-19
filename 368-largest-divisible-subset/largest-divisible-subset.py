class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        output=[]
        dp,parent=[1]*n,[i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i]=max(dp[i],dp[j]+1)
                    parent[i]=j
        last_index,maxi=0,max(dp)
        for i in range(n):
            if dp[i]==maxi:
                last_index=i
                break
        while parent[last_index]!=last_index:
            output.append(nums[last_index])
            last_index=parent[last_index]
        output.append(nums[last_index])
        return output