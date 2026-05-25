class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans= float('inf')
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            #if left half is sorted
            if(nums[l]<=nums[m]):
                ans=min(ans,nums[l])
                l=m+1
            #if right half is sorted
            elif(nums[m]<=nums[r]):
                ans=min(ans,nums[m])
                r=m-1
        return ans
