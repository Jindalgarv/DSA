class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pre,suf=[float('-inf')]*n,[float('inf')]*n
        pre[0],suf[n-1]=nums[0],nums[n-1]
        for i in range(1,n):
            pre[i]=max(pre[i-1],nums[i])
        for i in range(n-2,-1,-1):
            suf[i]=min(suf[i+1],nums[i])
        for i in range(n):
            if pre[i]-suf[i]<=k:
                return i
        return -1
        


        