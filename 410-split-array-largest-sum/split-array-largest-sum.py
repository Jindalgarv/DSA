class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        res=r
        def canSplit(mid):
            currSum,subArray=0,1
            for x in nums:
                currSum+=x
                if currSum<=mid:
                    continue
                else:
                    currSum=x
                    subArray+=1
            if subArray >k:
                return False
            return True

        while l<=r:
            mid=(l+r)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

