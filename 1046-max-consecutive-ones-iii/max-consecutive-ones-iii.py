class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l,r=0,0
        ans=0
        while r<n:
            if nums[r]:
                r+=1
            elif k>0:
                r+=1
                k-=1
            elif k==0:
                while nums[l] and l<=r:
                    l+=1
                k+=1
                l+=1
            ans=max(ans,r-l)
        return ans


        